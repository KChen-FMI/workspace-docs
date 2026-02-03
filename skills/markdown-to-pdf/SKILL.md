---
name: markdown-to-pdf
description: Convert Markdown (.md) or HTML (.html) to PDF using pandoc and/or wkhtmltopdf. Use when a user asks to export, print, or render Markdown to PDF, apply CSS/templates, add a table of contents, or standardize PDF output from docs.
---

# Markdown To Pdf

## Overview

Use this skill to convert Markdown to PDF with a reliable, repeatable workflow. Prefer pandoc for direct Markdown→PDF conversion and use wkhtmltopdf for HTML→PDF or when pandoc is unavailable.

## Quick Start

1. Check available tools:
   - `pandoc --version`
   - `wkhtmltopdf --version`
2. Run the script:

```bash
python scripts/convert_md_to_pdf.py --input doc.md --output doc.pdf
```

Common options:

```bash
python scripts/convert_md_to_pdf.py --input doc.md --output doc.pdf --toc --css style.css
python scripts/convert_md_to_pdf.py --input doc.md --output doc.pdf --engine pandoc --pdf-engine xelatex
python scripts/convert_md_to_pdf.py --input doc.html --output doc.pdf --engine wkhtmltopdf
```

## Workflow Decision Tree

1. If `pandoc` is available, use it for Markdown→PDF. It handles Markdown directly and supports templates, TOC, and metadata.
2. If `pandoc` is not available but `wkhtmltopdf` is:
   - Use wkhtmltopdf for HTML→PDF.
   - If input is `.md`, install pandoc or preconvert to HTML before wkhtmltopdf.
3. If neither is available, install one of them and retry.

## Script: `scripts/convert_md_to_pdf.py`

Use this wrapper to auto-select a converter and keep args consistent.

Arguments:

- `--input` (required): `.md` or `.html`
- `--output` (required): `.pdf`
- `--engine`: `auto` (default), `pandoc`, `wkhtmltopdf`
- `--css`: CSS file (pandoc: `--css`, wkhtmltopdf: `--user-style-sheet`)
- `--toc`: Pandoc table of contents
- `--template`: Pandoc template file
- `--pdf-engine`: Pandoc PDF engine (e.g., `xelatex`, `weasyprint`)
- `--title`: Document title
- `--metadata`: Pandoc metadata `key=value` (repeatable)
- `--pandoc-arg`: Extra pandoc arg (repeatable)
- `--wkhtmltopdf-arg`: Extra wkhtmltopdf arg (repeatable)

Examples:

```bash
python scripts/convert_md_to_pdf.py --input kitting-refactor-proposal-v2.md --output kitting-refactor-proposal-v2.pdf
python scripts/convert_md_to_pdf.py --input doc.md --output doc.pdf --toc --metadata author=Team
python scripts/convert_md_to_pdf.py --input doc.html --output doc.pdf --engine wkhtmltopdf --wkhtmltopdf-arg --enable-local-file-access
```

## Notes

Pandoc is the most reliable path for Markdown→PDF. Use wkhtmltopdf when you have HTML already or need its rendering quirks. If wkhtmltopdf is used with Markdown input, the script will require pandoc to preconvert to HTML.
