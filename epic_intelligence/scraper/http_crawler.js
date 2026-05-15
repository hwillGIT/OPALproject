/**
 * Epic Documentation HTTP Crawler
 *
 * Lightweight HTTP-based scraper using fetch + cheerio.
 * For pages without heavy JavaScript rendering.
 *
 * Usage:
 *   node http_crawler.js --site open_epic
 *   node http_crawler.js --url https://open.epic.com/DeveloperResources
 *   node http_crawler.js --all
 */

const fetch = require('node-fetch');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// Configuration
const CONFIG = {
  outputDir: path.join(__dirname, 'output'),
  rateLimit: 1500, // ms between requests
  maxRetries: 3,
  timeout: 30000,
  maxDepth: 4,
  maxPages: 500,
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
    contentSelector: 'main, .content, article, .documentation, #main-content, .container',
    excludePatterns: [
      /\/login/i,
      /\/register/i,
      /\/account/i,
      /\.(pdf|zip|exe|png|jpg|gif|svg)$/i,
      /javascript:/i,
      /#$/
    ],
    followExternal: false
  },
  fhir_epic: {
    name: 'Epic on FHIR',
    baseUrl: 'https://fhir.epic.com',
    startUrls: [
      '/Documentation',
      '/Specifications',
      '/FAQ'
    ],
    contentSelector: 'main, .content, article, .documentation, .spec-content, #main-content',
    excludePatterns: [
      /\/login/i,
      /\/sandbox/i,
      /\.(pdf|zip|exe|png|jpg|gif|svg)$/i
    ],
    followExternal: false
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
      '/task.html',
      '/coverage.html',
      '/resourcelist.html'
    ],
    contentSelector: '#segment-content, .col-12, main, body',
    excludePatterns: [
      /\/history/i,
      /\.(pdf|zip|xml|json|png|jpg|gif|svg)$/i,
      /examples\.html$/i
    ],
    followExternal: false
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
    contentSelector: 'main, article, .content, body',
    excludePatterns: [],
    followExternal: false
  },
  smart_app_launch: {
    name: 'SMART App Launch',
    baseUrl: 'https://build.fhir.org/ig/HL7/smart-app-launch',
    startUrls: [
      '/app-launch.html',
      '/scopes-and-launch-context.html',
      '/client-confidential-asymmetric.html',
      '/backend-services.html',
      '/toc.html'
    ],
    contentSelector: '#segment-content, .col-12, main, body',
    excludePatterns: [
      /\/history/i,
      /\.(pdf|zip|xml|json|png|jpg|gif|svg)$/i
    ],
    followExternal: false
  }
};

class HttpCrawler {
  constructor(siteConfig) {
    this.config = siteConfig;
    this.visited = new Set();
    this.queue = [];
    this.results = [];
    this.errors = [];
  }

  async init() {
    // Ensure output directories exist
    const siteName = this.config.name.toLowerCase().replace(/\s+/g, '_');
    const dirs = ['raw', 'markdown', 'structured'].map(d =>
      path.join(CONFIG.outputDir, d, siteName)
    );
    dirs.forEach(dir => fs.mkdirSync(dir, { recursive: true }));
  }

  generateFileId(url) {
    const hash = crypto.createHash('md5').update(url).digest('hex').slice(0, 8);
    const urlPath = new URL(url).pathname.replace(/[^a-zA-Z0-9]/g, '_').slice(0, 50);
    return `${urlPath}_${hash}`;
  }

  async delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  normalizeUrl(url, base) {
    try {
      const parsed = new URL(url, base);
      // Remove trailing slashes and hash fragments
      let normalized = parsed.origin + parsed.pathname;
      if (normalized.endsWith('/') && normalized.length > 1) {
        normalized = normalized.slice(0, -1);
      }
      // Keep query params for some sites
      if (parsed.search) {
        normalized += parsed.search;
      }
      return normalized;
    } catch {
      return null;
    }
  }

  isValidUrl(url) {
    try {
      const parsed = new URL(url);

      // Must be same origin
      if (!url.startsWith(this.config.baseUrl)) {
        return false;
      }

      // Check exclude patterns
      for (const pattern of this.config.excludePatterns) {
        if (pattern.test(url)) {
          return false;
        }
      }

      return true;
    } catch {
      return false;
    }
  }

  async fetchPage(url) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), CONFIG.timeout);

    try {
      const response = await fetch(url, {
        headers: {
          'User-Agent': CONFIG.userAgent,
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate',
          'Connection': 'keep-alive'
        },
        signal: controller.signal,
        redirect: 'follow'
      });

      clearTimeout(timeout);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const contentType = response.headers.get('content-type') || '';
      if (!contentType.includes('text/html') && !contentType.includes('application/xhtml')) {
        throw new Error(`Non-HTML content type: ${contentType}`);
      }

      return await response.text();
    } catch (err) {
      clearTimeout(timeout);
      throw err;
    }
  }

  extractLinks($, baseUrl) {
    const links = new Set();

    $('a[href]').each((_, el) => {
      const href = $(el).attr('href');
      if (!href) return;

      const normalized = this.normalizeUrl(href, baseUrl);
      if (normalized && this.isValidUrl(normalized)) {
        links.add(normalized);
      }
    });

    return Array.from(links);
  }

  extractContent($) {
    // Remove unwanted elements
    $('script, style, nav, header, footer, .nav, .navbar, .sidebar, .menu, .advertisement').remove();

    // Try to find main content
    let content = null;
    for (const selector of this.config.contentSelector.split(', ')) {
      const el = $(selector.trim());
      if (el.length > 0) {
        content = el.first();
        break;
      }
    }

    if (!content) {
      content = $('body');
    }

    return {
      html: content.html() || '',
      text: content.text().replace(/\s+/g, ' ').trim()
    };
  }

  extractMetadata($, url) {
    return {
      title: $('title').text().trim() || $('h1').first().text().trim() || 'Untitled',
      description: $('meta[name="description"]').attr('content') || '',
      keywords: $('meta[name="keywords"]').attr('content') || '',
      canonical: $('link[rel="canonical"]').attr('href') || url,
      headings: $('h1, h2, h3').map((_, el) => ({
        level: parseInt(el.tagName.slice(1)),
        text: $(el).text().trim()
      })).get()
    };
  }

  htmlToMarkdown(html, metadata, url) {
    let md = `# ${metadata.title}\n\n`;
    md += `> Source: ${url}\n`;
    if (metadata.description) {
      md += `> ${metadata.description}\n`;
    }
    md += `\n---\n\n`;

    // Remove scripts and styles
    html = html.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '');
    html = html.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');
    html = html.replace(/<!--[\s\S]*?-->/g, '');

    // Convert headings
    html = html.replace(/<h1[^>]*>([\s\S]*?)<\/h1>/gi, '\n# $1\n');
    html = html.replace(/<h2[^>]*>([\s\S]*?)<\/h2>/gi, '\n## $1\n');
    html = html.replace(/<h3[^>]*>([\s\S]*?)<\/h3>/gi, '\n### $1\n');
    html = html.replace(/<h4[^>]*>([\s\S]*?)<\/h4>/gi, '\n#### $1\n');
    html = html.replace(/<h5[^>]*>([\s\S]*?)<\/h5>/gi, '\n##### $1\n');
    html = html.replace(/<h6[^>]*>([\s\S]*?)<\/h6>/gi, '\n###### $1\n');

    // Convert code blocks - handle nested tags
    html = html.replace(/<pre[^>]*>[\s\S]*?<code[^>]*>([\s\S]*?)<\/code>[\s\S]*?<\/pre>/gi, '\n```\n$1\n```\n');
    html = html.replace(/<pre[^>]*>([\s\S]*?)<\/pre>/gi, '\n```\n$1\n```\n');
    html = html.replace(/<code[^>]*>(.*?)<\/code>/gi, '`$1`');

    // Convert lists
    html = html.replace(/<ul[^>]*>/gi, '\n');
    html = html.replace(/<\/ul>/gi, '\n');
    html = html.replace(/<ol[^>]*>/gi, '\n');
    html = html.replace(/<\/ol>/gi, '\n');
    html = html.replace(/<li[^>]*>([\s\S]*?)<\/li>/gi, '- $1\n');

    // Convert links
    html = html.replace(/<a[^>]*href="([^"]*)"[^>]*>([\s\S]*?)<\/a>/gi, '[$2]($1)');

    // Convert emphasis
    html = html.replace(/<strong[^>]*>([\s\S]*?)<\/strong>/gi, '**$1**');
    html = html.replace(/<b[^>]*>([\s\S]*?)<\/b>/gi, '**$1**');
    html = html.replace(/<em[^>]*>([\s\S]*?)<\/em>/gi, '*$1*');
    html = html.replace(/<i[^>]*>([\s\S]*?)<\/i>/gi, '*$1*');

    // Convert paragraphs and breaks
    html = html.replace(/<p[^>]*>([\s\S]*?)<\/p>/gi, '\n$1\n');
    html = html.replace(/<br\s*\/?>/gi, '\n');
    html = html.replace(/<hr\s*\/?>/gi, '\n---\n');
    html = html.replace(/<div[^>]*>/gi, '\n');
    html = html.replace(/<\/div>/gi, '\n');

    // Convert tables
    html = html.replace(/<table[^>]*>/gi, '\n');
    html = html.replace(/<\/table>/gi, '\n');
    html = html.replace(/<thead[^>]*>/gi, '');
    html = html.replace(/<\/thead>/gi, '');
    html = html.replace(/<tbody[^>]*>/gi, '');
    html = html.replace(/<\/tbody>/gi, '');
    html = html.replace(/<tr[^>]*>/gi, '| ');
    html = html.replace(/<\/tr>/gi, '|\n');
    html = html.replace(/<th[^>]*>([\s\S]*?)<\/th>/gi, '$1 | ');
    html = html.replace(/<td[^>]*>([\s\S]*?)<\/td>/gi, '$1 | ');

    // Convert definition lists
    html = html.replace(/<dl[^>]*>/gi, '\n');
    html = html.replace(/<\/dl>/gi, '\n');
    html = html.replace(/<dt[^>]*>([\s\S]*?)<\/dt>/gi, '\n**$1**\n');
    html = html.replace(/<dd[^>]*>([\s\S]*?)<\/dd>/gi, ': $1\n');

    // Convert blockquotes
    html = html.replace(/<blockquote[^>]*>([\s\S]*?)<\/blockquote>/gi, '\n> $1\n');

    // Remove remaining HTML tags
    html = html.replace(/<[^>]+>/g, '');

    // Clean up entities
    html = html.replace(/&nbsp;/g, ' ');
    html = html.replace(/&amp;/g, '&');
    html = html.replace(/&lt;/g, '<');
    html = html.replace(/&gt;/g, '>');
    html = html.replace(/&quot;/g, '"');
    html = html.replace(/&#39;/g, "'");
    html = html.replace(/&rsquo;/g, "'");
    html = html.replace(/&lsquo;/g, "'");
    html = html.replace(/&rdquo;/g, '"');
    html = html.replace(/&ldquo;/g, '"');
    html = html.replace(/&mdash;/g, '—');
    html = html.replace(/&ndash;/g, '–');
    html = html.replace(/&hellip;/g, '...');
    html = html.replace(/&copy;/g, '(c)');
    html = html.replace(/&reg;/g, '(R)');
    html = html.replace(/&trade;/g, '(TM)');

    // Clean up whitespace
    html = html.replace(/\n{3,}/g, '\n\n');
    html = html.replace(/[ \t]+/g, ' ');
    html = html.trim();

    return md + html;
  }

  async crawlPage(url, depth = 0) {
    if (depth > CONFIG.maxDepth) return null;
    if (this.visited.has(url)) return null;
    if (this.results.length >= CONFIG.maxPages) return null;

    this.visited.add(url);
    const pageNum = this.visited.size;
    console.log(`[${pageNum}/${CONFIG.maxPages}] Crawling: ${url} (depth: ${depth})`);

    let result = null;

    try {
      // Fetch with retry logic
      let html;
      let lastError;

      for (let attempt = 0; attempt < CONFIG.maxRetries; attempt++) {
        try {
          html = await this.fetchPage(url);
          break;
        } catch (err) {
          lastError = err;
          console.log(`  Retry ${attempt + 1}/${CONFIG.maxRetries}: ${err.message}`);
          await this.delay(CONFIG.rateLimit * (attempt + 1));
        }
      }

      if (!html) {
        throw lastError || new Error('Failed to fetch page');
      }

      // Parse HTML
      const $ = cheerio.load(html);

      // Extract content and metadata
      const content = this.extractContent($);
      const metadata = this.extractMetadata($, url);
      const links = this.extractLinks($, url);

      // Convert to Markdown
      const markdown = this.htmlToMarkdown(content.html, metadata, url);

      // Save results
      const fileId = this.generateFileId(url);
      const siteName = this.config.name.toLowerCase().replace(/\s+/g, '_');

      // Save raw HTML
      fs.writeFileSync(
        path.join(CONFIG.outputDir, 'raw', siteName, `${fileId}.html`),
        html
      );

      // Save markdown
      fs.writeFileSync(
        path.join(CONFIG.outputDir, 'markdown', siteName, `${fileId}.md`),
        markdown
      );

      // Save structured data
      const structured = {
        url: url,
        fileId: fileId,
        title: metadata.title,
        description: metadata.description,
        crawledAt: new Date().toISOString(),
        depth: depth,
        textLength: content.text.length,
        wordCount: content.text.split(/\s+/).length,
        links: links,
        headings: metadata.headings,
        siteName: this.config.name
      };

      fs.writeFileSync(
        path.join(CONFIG.outputDir, 'structured', siteName, `${fileId}.json`),
        JSON.stringify(structured, null, 2)
      );

      result = {
        url,
        fileId,
        title: metadata.title,
        links,
        depth,
        wordCount: structured.wordCount
      };

      this.results.push(result);
      console.log(`  -> ${metadata.title} (${structured.wordCount} words, ${links.length} links)`);

      // Queue new links for crawling
      for (const link of links) {
        if (!this.visited.has(link) && !this.queue.some(q => q.url === link)) {
          this.queue.push({ url: link, depth: depth + 1 });
        }
      }

    } catch (err) {
      console.error(`  Error: ${err.message}`);
      this.errors.push({ url, error: err.message, depth });
    }

    await this.delay(CONFIG.rateLimit);
    return result;
  }

  async crawlSite() {
    console.log(`\n${'='.repeat(60)}`);
    console.log(`Starting crawl of: ${this.config.name}`);
    console.log(`Base URL: ${this.config.baseUrl}`);
    console.log(`Max pages: ${CONFIG.maxPages}, Max depth: ${CONFIG.maxDepth}`);
    console.log(`${'='.repeat(60)}\n`);

    await this.init();

    // Add start URLs to queue
    for (const startPath of this.config.startUrls) {
      const url = startPath.startsWith('http')
        ? startPath
        : this.config.baseUrl + startPath;
      this.queue.push({ url, depth: 0 });
    }

    // Process queue
    while (this.queue.length > 0 && this.results.length < CONFIG.maxPages) {
      const { url, depth } = this.queue.shift();
      await this.crawlPage(url, depth);
    }

    // Save crawl summary
    const summary = {
      site: this.config.name,
      baseUrl: this.config.baseUrl,
      crawledAt: new Date().toISOString(),
      totalPages: this.results.length,
      totalErrors: this.errors.length,
      totalWords: this.results.reduce((sum, r) => sum + (r.wordCount || 0), 0),
      pages: this.results.map(r => ({
        url: r.url,
        title: r.title,
        fileId: r.fileId,
        depth: r.depth,
        wordCount: r.wordCount
      })),
      errors: this.errors
    };

    const siteName = this.config.name.toLowerCase().replace(/\s+/g, '_');
    fs.writeFileSync(
      path.join(CONFIG.outputDir, `${siteName}_summary.json`),
      JSON.stringify(summary, null, 2)
    );

    console.log(`\n${'='.repeat(60)}`);
    console.log(`Crawl complete: ${this.results.length} pages, ${this.errors.length} errors`);
    console.log(`Total words: ${summary.totalWords.toLocaleString()}`);
    console.log(`Summary saved to: ${siteName}_summary.json`);
    console.log(`${'='.repeat(60)}\n`);

    return summary;
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
      siteConfig.startUrls = [url.replace(config.baseUrl, '') || '/'];
      break;
    }
  }

  if (!siteConfig) {
    // Create generic config for unknown sites
    const parsed = new URL(url);
    siteConfig = {
      name: parsed.hostname.replace(/\./g, '_'),
      baseUrl: parsed.origin,
      startUrls: [parsed.pathname + parsed.search],
      contentSelector: 'main, article, .content, #content, .documentation, body',
      excludePatterns: [/\.(pdf|zip|exe|png|jpg|gif|svg)$/i],
      followExternal: false
    };
  }

  const crawler = new HttpCrawler(siteConfig);
  return await crawler.crawlSite();
}

// Main entry point
async function main() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.includes('-h')) {
    console.log(`
Epic Documentation HTTP Crawler

Usage:
  node http_crawler.js --site <site_name>    Crawl a specific site
  node http_crawler.js --url <url>           Crawl starting from a URL
  node http_crawler.js --all                 Crawl all configured sites
  node http_crawler.js --list                List available sites

Sites: ${Object.keys(SITES).join(', ')}

Options:
  --max-pages <n>    Maximum pages to crawl (default: ${CONFIG.maxPages})
  --max-depth <n>    Maximum link depth (default: ${CONFIG.maxDepth})
`);
    return;
  }

  if (args.includes('--list')) {
    console.log('Available sites:');
    for (const [key, config] of Object.entries(SITES)) {
      console.log(`  ${key}: ${config.name} (${config.baseUrl})`);
      console.log(`    Start URLs: ${config.startUrls.join(', ')}`);
    }
    return;
  }

  // Parse optional config overrides
  const maxPagesIdx = args.indexOf('--max-pages');
  if (maxPagesIdx !== -1 && args[maxPagesIdx + 1]) {
    CONFIG.maxPages = parseInt(args[maxPagesIdx + 1]);
  }

  const maxDepthIdx = args.indexOf('--max-depth');
  if (maxDepthIdx !== -1 && args[maxDepthIdx + 1]) {
    CONFIG.maxDepth = parseInt(args[maxDepthIdx + 1]);
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
    const crawler = new HttpCrawler(SITES[siteName]);
    await crawler.crawlSite();
    return;
  }

  if (args.includes('--all')) {
    const results = [];
    for (const [key, config] of Object.entries(SITES)) {
      console.log(`\n>>> Starting: ${config.name} <<<\n`);
      const crawler = new HttpCrawler(config);
      const result = await crawler.crawlSite();
      results.push(result);
    }

    // Save combined summary
    const combined = {
      crawledAt: new Date().toISOString(),
      totalSites: results.length,
      totalPages: results.reduce((sum, r) => sum + r.totalPages, 0),
      totalWords: results.reduce((sum, r) => sum + r.totalWords, 0),
      sites: results.map(r => ({
        name: r.site,
        pages: r.totalPages,
        words: r.totalWords,
        errors: r.totalErrors
      }))
    };

    fs.writeFileSync(
      path.join(CONFIG.outputDir, 'all_sites_summary.json'),
      JSON.stringify(combined, null, 2)
    );

    console.log('\n' + '='.repeat(60));
    console.log('ALL SITES COMPLETE');
    console.log(`Total: ${combined.totalPages} pages, ${combined.totalWords.toLocaleString()} words`);
    console.log('='.repeat(60));
    return;
  }

  // Default: show help
  console.log('Use --help for usage information');
}

// Export for module use
module.exports = { HttpCrawler, SITES, crawlSingleUrl };

// Run if called directly
if (require.main === module) {
  main().catch(console.error);
}
