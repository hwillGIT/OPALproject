/**
 * Epic Documentation Playwright Crawler
 *
 * Comprehensive scraper for Epic EHR documentation using Playwright.
 * Handles JavaScript-rendered content, rate limiting, and recursive crawling.
 *
 * Usage:
 *   node playwright_crawler.js --site fhir_epic
 *   node playwright_crawler.js --url https://open.epic.com/DeveloperResources
 *   node playwright_crawler.js --all
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// Configuration
const CONFIG = {
  outputDir: path.join(__dirname, 'output'),
  rateLimit: 2000, // ms between requests
  maxRetries: 3,
  timeout: 30000,
  maxDepth: 5,
  userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
};

// Site configurations
const SITES = {
  open_epic: {
    name: 'Open Epic',
    baseUrl: 'https://open.epic.com',
    startUrls: [
      '/DeveloperResources',
      '/Playbooks',
      '/Interface/FHIR',
      '/TechnicalSpecifications'
    ],
    linkSelector: 'a[href]',
    contentSelector: 'main, .content, article, .documentation',
    excludePatterns: [
      /\/login/i,
      /\/register/i,
      /\/account/i,
      /\.(pdf|zip|exe)$/i
    ]
  },
  fhir_epic: {
    name: 'Epic on FHIR',
    baseUrl: 'https://fhir.epic.com',
    startUrls: [
      '/Documentation',
      '/Specifications',
      '/FAQ'
    ],
    linkSelector: 'a[href]',
    contentSelector: 'main, .content, article, .documentation, .spec-content',
    excludePatterns: [
      /\/login/i,
      /\/sandbox/i,
      /\.(pdf|zip|exe)$/i
    ]
  },
  hl7_fhir: {
    name: 'HL7 FHIR R4',
    baseUrl: 'https://hl7.org/fhir/R4',
    startUrls: [
      '/patient.html',
      '/observation.html',
      '/condition.html',
      '/medicationrequest.html',
      '/allergyintolerance.html',
      '/encounter.html',
      '/documentreference.html',
      '/practitioner.html',
      '/organization.html',
      '/appointment.html',
      '/resourcelist.html'
    ],
    linkSelector: 'a[href]',
    contentSelector: '#segment-content, .col-12',
    excludePatterns: [
      /\/history/i,
      /\.(pdf|zip|xml|json)$/i
    ]
  },
  cds_hooks: {
    name: 'CDS Hooks',
    baseUrl: 'https://cds-hooks.hl7.org',
    startUrls: [
      '/2.0/',
      '/hooks/patient-view/',
      '/hooks/order-select/',
      '/hooks/order-sign/'
    ],
    linkSelector: 'a[href]',
    contentSelector: 'main, article, .content',
    excludePatterns: []
  },
  smart_app_launch: {
    name: 'SMART App Launch',
    baseUrl: 'https://build.fhir.org/ig/HL7/smart-app-launch',
    startUrls: [
      '/app-launch.html',
      '/scopes-and-launch-context.html',
      '/client-confidential-asymmetric.html',
      '/backend-services.html'
    ],
    linkSelector: 'a[href]',
    contentSelector: '#segment-content, .col-12, main',
    excludePatterns: [
      /\/history/i,
      /\.(pdf|zip|xml|json)$/i
    ]
  }
};

class EpicCrawler {
  constructor(siteConfig) {
    this.config = siteConfig;
    this.visited = new Set();
    this.queue = [];
    this.results = [];
    this.browser = null;
    this.context = null;
  }

  async init() {
    this.browser = await chromium.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    this.context = await this.browser.newContext({
      userAgent: CONFIG.userAgent,
      viewport: { width: 1920, height: 1080 }
    });

    // Ensure output directories exist
    const dirs = ['raw', 'markdown', 'structured'].map(d =>
      path.join(CONFIG.outputDir, d, this.config.name.toLowerCase().replace(/\s+/g, '_'))
    );
    dirs.forEach(dir => fs.mkdirSync(dir, { recursive: true }));
  }

  async close() {
    if (this.browser) {
      await this.browser.close();
    }
  }

  generateFileId(url) {
    const hash = crypto.createHash('md5').update(url).digest('hex').slice(0, 8);
    const urlPath = new URL(url).pathname.replace(/[^a-zA-Z0-9]/g, '_').slice(0, 50);
    return `${urlPath}_${hash}`;
  }

  async delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  isValidUrl(url) {
    try {
      const parsed = new URL(url, this.config.baseUrl);

      // Must be same origin or start with base URL
      if (!parsed.href.startsWith(this.config.baseUrl)) {
        return false;
      }

      // Check exclude patterns
      for (const pattern of this.config.excludePatterns) {
        if (pattern.test(parsed.href)) {
          return false;
        }
      }

      return true;
    } catch {
      return false;
    }
  }

  async crawlPage(url, depth = 0) {
    if (depth > CONFIG.maxDepth) return null;
    if (this.visited.has(url)) return null;

    this.visited.add(url);
    console.log(`[${this.visited.size}] Crawling: ${url} (depth: ${depth})`);

    const page = await this.context.newPage();
    let result = null;

    try {
      // Navigate with retry logic
      let lastError;
      for (let attempt = 0; attempt < CONFIG.maxRetries; attempt++) {
        try {
          await page.goto(url, {
            waitUntil: 'networkidle',
            timeout: CONFIG.timeout
          });
          break;
        } catch (err) {
          lastError = err;
          console.log(`  Retry ${attempt + 1}/${CONFIG.maxRetries}: ${err.message}`);
          await this.delay(CONFIG.rateLimit * (attempt + 1));
        }
      }

      if (lastError && !page.url().includes(new URL(url).pathname)) {
        throw lastError;
      }

      // Wait for content to load
      await page.waitForLoadState('domcontentloaded');
      await this.delay(500); // Extra wait for dynamic content

      // Extract page content
      const content = await page.evaluate((selector) => {
        const el = document.querySelector(selector) || document.body;
        return {
          title: document.title,
          html: el.innerHTML,
          text: el.innerText,
          url: window.location.href
        };
      }, this.config.contentSelector);

      // Extract links for recursive crawling
      const links = await page.evaluate((selector, baseUrl) => {
        const anchors = document.querySelectorAll(selector);
        return Array.from(anchors)
          .map(a => a.href)
          .filter(href => href && !href.startsWith('javascript:') && !href.startsWith('#'));
      }, this.config.linkSelector, this.config.baseUrl);

      // Convert HTML to Markdown (basic conversion)
      const markdown = this.htmlToMarkdown(content.html, content.title, url);

      // Save results
      const fileId = this.generateFileId(url);
      const siteName = this.config.name.toLowerCase().replace(/\s+/g, '_');

      // Save raw HTML
      fs.writeFileSync(
        path.join(CONFIG.outputDir, 'raw', siteName, `${fileId}.html`),
        content.html
      );

      // Save markdown
      fs.writeFileSync(
        path.join(CONFIG.outputDir, 'markdown', siteName, `${fileId}.md`),
        markdown
      );

      // Save structured data
      const structured = {
        url: url,
        title: content.title,
        crawledAt: new Date().toISOString(),
        textLength: content.text.length,
        links: links.filter(l => this.isValidUrl(l)),
        sections: this.extractSections(content.html)
      };

      fs.writeFileSync(
        path.join(CONFIG.outputDir, 'structured', siteName, `${fileId}.json`),
        JSON.stringify(structured, null, 2)
      );

      result = {
        url,
        title: content.title,
        fileId,
        links: structured.links,
        depth
      };

      this.results.push(result);

      // Queue new links for crawling
      for (const link of structured.links) {
        if (!this.visited.has(link) && !this.queue.includes(link)) {
          this.queue.push({ url: link, depth: depth + 1 });
        }
      }

    } catch (err) {
      console.error(`  Error crawling ${url}: ${err.message}`);
    } finally {
      await page.close();
      await this.delay(CONFIG.rateLimit);
    }

    return result;
  }

  htmlToMarkdown(html, title, url) {
    // Basic HTML to Markdown conversion
    let md = `# ${title}\n\nSource: ${url}\n\n---\n\n`;

    // Remove scripts and styles
    html = html.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '');
    html = html.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');

    // Convert headings
    html = html.replace(/<h1[^>]*>(.*?)<\/h1>/gi, '\n# $1\n');
    html = html.replace(/<h2[^>]*>(.*?)<\/h2>/gi, '\n## $1\n');
    html = html.replace(/<h3[^>]*>(.*?)<\/h3>/gi, '\n### $1\n');
    html = html.replace(/<h4[^>]*>(.*?)<\/h4>/gi, '\n#### $1\n');
    html = html.replace(/<h5[^>]*>(.*?)<\/h5>/gi, '\n##### $1\n');
    html = html.replace(/<h6[^>]*>(.*?)<\/h6>/gi, '\n###### $1\n');

    // Convert code blocks
    html = html.replace(/<pre[^>]*><code[^>]*>([\s\S]*?)<\/code><\/pre>/gi, '\n```\n$1\n```\n');
    html = html.replace(/<pre[^>]*>([\s\S]*?)<\/pre>/gi, '\n```\n$1\n```\n');
    html = html.replace(/<code[^>]*>(.*?)<\/code>/gi, '`$1`');

    // Convert lists
    html = html.replace(/<ul[^>]*>/gi, '\n');
    html = html.replace(/<\/ul>/gi, '\n');
    html = html.replace(/<ol[^>]*>/gi, '\n');
    html = html.replace(/<\/ol>/gi, '\n');
    html = html.replace(/<li[^>]*>(.*?)<\/li>/gi, '- $1\n');

    // Convert links
    html = html.replace(/<a[^>]*href="([^"]*)"[^>]*>(.*?)<\/a>/gi, '[$2]($1)');

    // Convert emphasis
    html = html.replace(/<strong[^>]*>(.*?)<\/strong>/gi, '**$1**');
    html = html.replace(/<b[^>]*>(.*?)<\/b>/gi, '**$1**');
    html = html.replace(/<em[^>]*>(.*?)<\/em>/gi, '*$1*');
    html = html.replace(/<i[^>]*>(.*?)<\/i>/gi, '*$1*');

    // Convert paragraphs and line breaks
    html = html.replace(/<p[^>]*>(.*?)<\/p>/gi, '\n$1\n');
    html = html.replace(/<br\s*\/?>/gi, '\n');
    html = html.replace(/<hr\s*\/?>/gi, '\n---\n');

    // Convert tables (basic)
    html = html.replace(/<table[^>]*>/gi, '\n');
    html = html.replace(/<\/table>/gi, '\n');
    html = html.replace(/<tr[^>]*>/gi, '| ');
    html = html.replace(/<\/tr>/gi, '|\n');
    html = html.replace(/<th[^>]*>(.*?)<\/th>/gi, '$1 | ');
    html = html.replace(/<td[^>]*>(.*?)<\/td>/gi, '$1 | ');

    // Remove remaining HTML tags
    html = html.replace(/<[^>]+>/g, '');

    // Clean up entities
    html = html.replace(/&nbsp;/g, ' ');
    html = html.replace(/&amp;/g, '&');
    html = html.replace(/&lt;/g, '<');
    html = html.replace(/&gt;/g, '>');
    html = html.replace(/&quot;/g, '"');
    html = html.replace(/&#39;/g, "'");

    // Clean up whitespace
    html = html.replace(/\n{3,}/g, '\n\n');
    html = html.trim();

    return md + html;
  }

  extractSections(html) {
    const sections = [];
    const headingRegex = /<h([1-6])[^>]*>(.*?)<\/h\1>/gi;
    let match;

    while ((match = headingRegex.exec(html)) !== null) {
      sections.push({
        level: parseInt(match[1]),
        title: match[2].replace(/<[^>]+>/g, '').trim()
      });
    }

    return sections;
  }

  async crawlSite() {
    console.log(`\n${'='.repeat(60)}`);
    console.log(`Starting crawl of: ${this.config.name}`);
    console.log(`Base URL: ${this.config.baseUrl}`);
    console.log(`${'='.repeat(60)}\n`);

    await this.init();

    try {
      // Add start URLs to queue
      for (const startPath of this.config.startUrls) {
        const url = this.config.baseUrl + startPath;
        this.queue.push({ url, depth: 0 });
      }

      // Process queue
      while (this.queue.length > 0) {
        const { url, depth } = this.queue.shift();
        await this.crawlPage(url, depth);
      }

      // Save crawl summary
      const summary = {
        site: this.config.name,
        baseUrl: this.config.baseUrl,
        crawledAt: new Date().toISOString(),
        totalPages: this.results.length,
        pages: this.results.map(r => ({
          url: r.url,
          title: r.title,
          fileId: r.fileId
        }))
      };

      const siteName = this.config.name.toLowerCase().replace(/\s+/g, '_');
      fs.writeFileSync(
        path.join(CONFIG.outputDir, `${siteName}_summary.json`),
        JSON.stringify(summary, null, 2)
      );

      console.log(`\nCrawl complete: ${this.results.length} pages`);
      return summary;

    } finally {
      await this.close();
    }
  }
}

// Single URL crawler
async function crawlSingleUrl(url) {
  console.log(`Crawling single URL: ${url}`);

  // Determine which site config to use
  let siteConfig = null;
  for (const [key, config] of Object.entries(SITES)) {
    if (url.startsWith(config.baseUrl)) {
      siteConfig = { ...config };
      siteConfig.startUrls = [url.replace(config.baseUrl, '')];
      break;
    }
  }

  if (!siteConfig) {
    // Create generic config for unknown sites
    const parsed = new URL(url);
    siteConfig = {
      name: parsed.hostname,
      baseUrl: parsed.origin,
      startUrls: [parsed.pathname],
      linkSelector: 'a[href]',
      contentSelector: 'main, article, .content, body',
      excludePatterns: [/\.(pdf|zip|exe)$/i]
    };
  }

  const crawler = new EpicCrawler(siteConfig);
  return await crawler.crawlSite();
}

// Main entry point
async function main() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.includes('-h')) {
    console.log(`
Epic Documentation Crawler

Usage:
  node playwright_crawler.js --site <site_name>    Crawl a specific site
  node playwright_crawler.js --url <url>           Crawl a single URL recursively
  node playwright_crawler.js --all                 Crawl all configured sites
  node playwright_crawler.js --list                List available sites

Sites: ${Object.keys(SITES).join(', ')}
`);
    return;
  }

  if (args.includes('--list')) {
    console.log('Available sites:');
    for (const [key, config] of Object.entries(SITES)) {
      console.log(`  ${key}: ${config.name} (${config.baseUrl})`);
    }
    return;
  }

  const urlIndex = args.indexOf('--url');
  if (urlIndex !== -1 && args[urlIndex + 1]) {
    await crawlSingleUrl(args[urlIndex + 1]);
    return;
  }

  const siteIndex = args.indexOf('--site');
  if (siteIndex !== -1 && args[siteIndex + 1]) {
    const siteName = args[siteIndex + 1];
    if (!SITES[siteName]) {
      console.error(`Unknown site: ${siteName}`);
      console.log(`Available: ${Object.keys(SITES).join(', ')}`);
      process.exit(1);
    }
    const crawler = new EpicCrawler(SITES[siteName]);
    await crawler.crawlSite();
    return;
  }

  if (args.includes('--all')) {
    const results = [];
    for (const [key, config] of Object.entries(SITES)) {
      const crawler = new EpicCrawler(config);
      const result = await crawler.crawlSite();
      results.push(result);
    }

    // Save combined summary
    fs.writeFileSync(
      path.join(CONFIG.outputDir, 'all_sites_summary.json'),
      JSON.stringify({
        crawledAt: new Date().toISOString(),
        sites: results
      }, null, 2)
    );
    return;
  }

  // Default: show help
  console.log('Use --help for usage information');
}

// Export for module use
module.exports = { EpicCrawler, SITES, crawlSingleUrl };

// Run if called directly
if (require.main === module) {
  main().catch(console.error);
}
