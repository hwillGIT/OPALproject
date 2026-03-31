"""
Epic Documentation Chunker

Intelligent chunking for Epic EHR documentation with:
- Section-aware splitting
- Code block preservation
- Overlap for context continuity
- Metadata extraction
"""

import re
import json
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class Chunk:
    """Represents a document chunk for embedding."""
    id: str
    source_file: str
    source_url: str
    title: str
    section_path: list[str]
    chunk_index: int
    total_chunks: int
    content: str
    token_estimate: int
    metadata: dict

    def to_dict(self) -> dict:
        return asdict(self)


class EpicDocChunker:
    """
    Chunks Epic documentation for vector embedding.

    Strategies:
    - Respect section boundaries (headers)
    - Preserve code blocks intact
    - Maintain overlap for context
    - Extract entity references (APIs, resources)
    """

    # Chunking configurations by content type
    CONFIGS = {
        "default": {
            "chunk_size": 1500,  # tokens (approx)
            "chunk_overlap": 200,
            "min_chunk_size": 100,
            "chars_per_token": 4  # rough estimate
        },
        "api_reference": {
            "chunk_size": 1000,
            "chunk_overlap": 150,
            "min_chunk_size": 50,
            "chars_per_token": 4
        },
        "code_example": {
            "chunk_size": 800,
            "chunk_overlap": 100,
            "min_chunk_size": 30,
            "chars_per_token": 3.5
        },
        "playbook": {
            "chunk_size": 2000,
            "chunk_overlap": 300,
            "min_chunk_size": 100,
            "chars_per_token": 4
        }
    }

    # Patterns for entity extraction
    PATTERNS = {
        "fhir_resource": re.compile(
            r'\b(Patient|Observation|Condition|MedicationRequest|MedicationStatement|'
            r'AllergyIntolerance|Immunization|Procedure|DiagnosticReport|DocumentReference|'
            r'Encounter|Appointment|Schedule|Slot|Task|ServiceRequest|Coverage|Claim|'
            r'ExplanationOfBenefit|Practitioner|Organization|Location|CarePlan|CareTeam|'
            r'Goal|Binary|Bundle|OperationOutcome|CapabilityStatement)\b'
        ),
        "epic_api": re.compile(
            r'([A-Z][a-zA-Z]+)\.(Read|Search|Create|Update|Delete|Patch)\s*\([^)]*\)'
        ),
        "oauth_scope": re.compile(
            r'(patient|user|system)/[A-Za-z]+\.(read|write|r|w|rs|ws|\*)'
        ),
        "http_endpoint": re.compile(
            r'(GET|POST|PUT|DELETE|PATCH)\s+(/api/FHIR/[^\s]+|/[a-z]+/[^\s]+)'
        ),
        "cds_hook": re.compile(
            r'(patient-view|order-select|order-sign|appointment-book|encounter-start|encounter-discharge)'
        ),
        "fhir_version": re.compile(
            r'\b(FHIR\s*R4|FHIR\s*R5|DSTU2|STU3|R4|R5)\b', re.IGNORECASE
        ),
        "uscdi_version": re.compile(
            r'\bUSCDI\s*(v[0-9]+|Version\s*[0-9]+)\b', re.IGNORECASE
        )
    }

    def __init__(self, config_name: str = "default"):
        self.config = self.CONFIGS.get(config_name, self.CONFIGS["default"])

    def estimate_tokens(self, text: str) -> int:
        """Estimate token count from character count."""
        return len(text) // self.config["chars_per_token"]

    def extract_entities(self, text: str) -> dict:
        """Extract Epic-related entities from text."""
        entities = {}
        for name, pattern in self.PATTERNS.items():
            matches = pattern.findall(text)
            if matches:
                # Flatten tuples from groups
                flat = []
                for m in matches:
                    if isinstance(m, tuple):
                        flat.append('.'.join(filter(None, m)))
                    else:
                        flat.append(m)
                entities[name] = list(set(flat))
        return entities

    def extract_sections(self, markdown: str) -> list[tuple[str, str, int]]:
        """
        Extract sections from markdown based on headers.

        Returns: [(section_title, content, level), ...]
        """
        sections = []
        lines = markdown.split('\n')
        current_section = []
        current_title = "Introduction"
        current_level = 0

        header_pattern = re.compile(r'^(#{1,6})\s+(.+)$')

        for line in lines:
            match = header_pattern.match(line)
            if match:
                # Save previous section
                if current_section:
                    content = '\n'.join(current_section).strip()
                    if content:
                        sections.append((current_title, content, current_level))

                # Start new section
                current_level = len(match.group(1))
                current_title = match.group(2).strip()
                current_section = []
            else:
                current_section.append(line)

        # Save final section
        if current_section:
            content = '\n'.join(current_section).strip()
            if content:
                sections.append((current_title, content, current_level))

        return sections

    def preserve_code_blocks(self, text: str) -> tuple[str, dict]:
        """
        Replace code blocks with placeholders to preserve them during chunking.

        Returns: (text_with_placeholders, {placeholder: code_block})
        """
        code_blocks = {}
        counter = 0

        def replace_block(match):
            nonlocal counter
            placeholder = f"__CODE_BLOCK_{counter}__"
            code_blocks[placeholder] = match.group(0)
            counter += 1
            return placeholder

        # Match fenced code blocks
        pattern = re.compile(r'```[\s\S]*?```', re.MULTILINE)
        text_with_placeholders = pattern.sub(replace_block, text)

        return text_with_placeholders, code_blocks

    def restore_code_blocks(self, text: str, code_blocks: dict) -> str:
        """Restore code blocks from placeholders."""
        for placeholder, code in code_blocks.items():
            text = text.replace(placeholder, code)
        return text

    def chunk_text(self, text: str, max_chars: int, overlap_chars: int) -> list[str]:
        """
        Split text into chunks respecting paragraph boundaries.
        """
        if len(text) <= max_chars:
            return [text]

        chunks = []
        paragraphs = re.split(r'\n\n+', text)
        current_chunk = []
        current_length = 0

        for para in paragraphs:
            para_length = len(para) + 2  # +2 for paragraph separator

            if current_length + para_length > max_chars and current_chunk:
                # Save current chunk
                chunk_text = '\n\n'.join(current_chunk)
                chunks.append(chunk_text)

                # Start new chunk with overlap
                overlap_text = chunk_text[-overlap_chars:] if len(chunk_text) > overlap_chars else ""
                if overlap_text:
                    # Find paragraph boundary in overlap
                    overlap_start = overlap_text.find('\n\n')
                    if overlap_start != -1:
                        overlap_text = overlap_text[overlap_start + 2:]

                current_chunk = [overlap_text, para] if overlap_text else [para]
                current_length = len(overlap_text) + para_length
            else:
                current_chunk.append(para)
                current_length += para_length

        # Save final chunk
        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))

        return chunks

    def chunk_document(
        self,
        markdown: str,
        source_file: str,
        source_url: str = "",
        doc_title: str = ""
    ) -> list[Chunk]:
        """
        Chunk a markdown document into embeddable pieces.

        Args:
            markdown: The markdown content
            source_file: Path to source file
            source_url: Original URL if known
            doc_title: Document title

        Returns:
            List of Chunk objects
        """
        chunks = []
        chunk_index = 0

        # Extract sections
        sections = self.extract_sections(markdown)

        # Calculate max chars from token target
        max_chars = self.config["chunk_size"] * self.config["chars_per_token"]
        overlap_chars = self.config["chunk_overlap"] * self.config["chars_per_token"]
        min_chars = self.config["min_chunk_size"] * self.config["chars_per_token"]

        # Track section path for hierarchy
        section_path = []

        for section_title, content, level in sections:
            # Update section path
            while len(section_path) >= level:
                if section_path:
                    section_path.pop()
            section_path.append(section_title)

            # Preserve code blocks
            content_safe, code_blocks = self.preserve_code_blocks(content)

            # Chunk the content
            text_chunks = self.chunk_text(content_safe, max_chars, overlap_chars)

            for text in text_chunks:
                # Skip too-small chunks
                if len(text) < min_chars:
                    continue

                # Restore code blocks
                final_text = self.restore_code_blocks(text, code_blocks)

                # Extract entities
                entities = self.extract_entities(final_text)

                # Create chunk
                chunk = Chunk(
                    id=f"{Path(source_file).stem}_{chunk_index}",
                    source_file=source_file,
                    source_url=source_url,
                    title=doc_title or section_title,
                    section_path=list(section_path),
                    chunk_index=chunk_index,
                    total_chunks=0,  # Updated after all chunks created
                    content=final_text,
                    token_estimate=self.estimate_tokens(final_text),
                    metadata={
                        "section_title": section_title,
                        "section_level": level,
                        "entities": entities,
                        "has_code": "```" in final_text,
                        "word_count": len(final_text.split())
                    }
                )
                chunks.append(chunk)
                chunk_index += 1

        # Update total_chunks
        for chunk in chunks:
            chunk.total_chunks = len(chunks)

        return chunks

    def chunk_directory(
        self,
        input_dir: Path,
        output_dir: Path,
        file_pattern: str = "*.md"
    ) -> dict:
        """
        Chunk all markdown files in a directory.

        Args:
            input_dir: Directory containing markdown files
            output_dir: Directory to save chunked JSON
            file_pattern: Glob pattern for files

        Returns:
            Summary statistics
        """
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        stats = {
            "files_processed": 0,
            "total_chunks": 0,
            "total_tokens": 0,
            "entities_found": {}
        }

        for md_file in input_path.glob(file_pattern):
            # Read markdown
            content = md_file.read_text(encoding='utf-8', errors='ignore')

            # Try to load associated metadata
            json_file = md_file.with_suffix('.json')
            metadata = {}
            if json_file.exists():
                try:
                    metadata = json.loads(json_file.read_text())
                except:
                    pass

            # Chunk document
            chunks = self.chunk_document(
                markdown=content,
                source_file=str(md_file),
                source_url=metadata.get('url', ''),
                doc_title=metadata.get('title', '')
            )

            # Save chunks
            output_file = output_path / f"{md_file.stem}_chunks.json"
            with open(output_file, 'w') as f:
                json.dump([c.to_dict() for c in chunks], f, indent=2)

            # Update stats
            stats["files_processed"] += 1
            stats["total_chunks"] += len(chunks)
            stats["total_tokens"] += sum(c.token_estimate for c in chunks)

            # Aggregate entities
            for chunk in chunks:
                for entity_type, entities in chunk.metadata.get("entities", {}).items():
                    if entity_type not in stats["entities_found"]:
                        stats["entities_found"][entity_type] = set()
                    stats["entities_found"][entity_type].update(entities)

        # Convert sets to lists for JSON serialization
        stats["entities_found"] = {
            k: list(v) for k, v in stats["entities_found"].items()
        }

        # Save stats
        stats_file = output_path / "_chunking_stats.json"
        with open(stats_file, 'w') as f:
            json.dump(stats, f, indent=2)

        return stats


def main():
    """CLI for chunking Epic documentation."""
    import argparse

    parser = argparse.ArgumentParser(description="Chunk Epic documentation for embedding")
    parser.add_argument("input_dir", help="Directory containing markdown files")
    parser.add_argument("output_dir", help="Directory to save chunked JSON")
    parser.add_argument("--config", choices=list(EpicDocChunker.CONFIGS.keys()),
                        default="default", help="Chunking configuration")
    parser.add_argument("--pattern", default="*.md", help="File pattern to match")

    args = parser.parse_args()

    chunker = EpicDocChunker(config_name=args.config)
    stats = chunker.chunk_directory(
        Path(args.input_dir),
        Path(args.output_dir),
        args.pattern
    )

    print(f"\nChunking complete:")
    print(f"  Files processed: {stats['files_processed']}")
    print(f"  Total chunks: {stats['total_chunks']}")
    print(f"  Total tokens (est): {stats['total_tokens']:,}")
    print(f"\nEntities found:")
    for entity_type, entities in stats['entities_found'].items():
        print(f"  {entity_type}: {len(entities)}")


if __name__ == "__main__":
    main()
