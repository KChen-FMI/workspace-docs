# Repository Guidelines

## Project Structure & Module Organization
このセクションでは、リポジトリ内の主要フォルダと役割を把握できます。
This repository is documentation-first. Major topic areas are organized by folder:
- `Azure-refactoring/`: Azure migration notes, network diagrams, and server planning docs.
- `run-book/`: operational run books, drafts, archived POCs, and supporting artifacts.
- `FMI_Env/`: system/environment diagrams, including Mermaid source under `FMI_Env/mermaid/`.
- `it-kb-db/`: Knowledge DB specs and MVP definition.
- `mobile-app-verification/`: deployment/security notes and validation scripts.
- `skills/`: reusable tooling such as Markdown-to-PDF conversion helpers.

Keep new files in the closest domain folder; avoid creating broad top-level folders unless a new workstream is established.

## Build, Test, and Development Commands
このセクションでは、日常的に使う確認・変換・検証コマンドを示します。
No single project build exists; use task-specific commands:
- `rg --files`: quickly inventory repository files.
- `python skills/markdown-to-pdf/scripts/convert_md_to_pdf.py --input <doc.md> --output <doc.pdf>`: convert Markdown/HTML to PDF (requires `pandoc` or `wkhtmltopdf`).
- `pwsh mobile-app-verification/scripts/check-intune-settings.ps1`: run read-only Intune/Entra checks (requires Microsoft Graph modules and auth).

## Coding Style & Naming Conventions
このセクションでは、Markdown とスクリプトの記述ルールを統一するための基準を示します。
- Markdown: use clear heading hierarchy (`#`, `##`, `###`) and concise bullet lists.
- Prefer UTF-8 Markdown (`.md`) for authored content; keep generated binaries (`.pdf`, `.png`) alongside source when needed for review.
- Naming: descriptive, topic-first filenames (for example, `Migration-Plan.md`, `service-catalog-data-sources.md`).
- Scripts: keep PowerShell in `.ps1`, Python in `.py`, and include usage examples at file top for nontrivial scripts.

## Testing Guidelines
このセクションでは、自動テストがない前提での実務的な確認方法を定義します。
There is no global automated test suite. Validate by type:
- For docs, check links, section flow, and diagram rendering.
- For scripts, run with safe/read-only options first and capture terminal output in the PR description.
- For generated artifacts, verify the source file and output file are both updated.

## Commit & Pull Request Guidelines
このセクションでは、履歴とレビュー効率を保つためのコミット・PR運用をまとめます。
Recent history uses short, action-oriented commit subjects (for example, `Add Azure refactoring docs and migration plan`, `merge folder`).
- Use imperative, scoped messages: `Add run-book data source summary`.
- Keep commits focused to one topic/workstream.
- PRs should include: purpose, changed folders, validation steps/commands run, and screenshots or output samples when diagrams/PDFs change.
