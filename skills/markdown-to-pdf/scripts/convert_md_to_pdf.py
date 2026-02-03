#!/usr/bin/env python
"""Convert Markdown or HTML to PDF using pandoc or wkhtmltopdf.

Usage examples:
  python scripts/convert_md_to_pdf.py --input doc.md --output doc.pdf
  python scripts/convert_md_to_pdf.py --input doc.md --output doc.pdf --toc --css style.css
  python scripts/convert_md_to_pdf.py --input doc.html --output doc.pdf --engine wkhtmltopdf
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile


def find_exe(name: str) -> str | None:
    return shutil.which(name)


def run(cmd: list[str]) -> None:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.returncode)


def build_pandoc_cmd(args: argparse.Namespace, input_path: str, output_path: str) -> list[str]:
    cmd = ["pandoc", input_path, "-o", output_path]
    if args.toc:
        cmd.append("--toc")
    if args.css:
        cmd.extend(["--css", args.css])
    if args.template:
        cmd.extend(["--template", args.template])
    if args.pdf_engine:
        cmd.extend(["--pdf-engine", args.pdf_engine])
    if args.title:
        cmd.extend(["-M", f"title={args.title}"])
    for meta in args.metadata:
        cmd.extend(["-M", meta])
    for extra in args.pandoc_arg:
        cmd.append(extra)
    return cmd


def build_wkhtmltopdf_cmd(args: argparse.Namespace, input_path: str, output_path: str) -> list[str]:
    cmd = ["wkhtmltopdf"]
    if args.title:
        cmd.extend(["--title", args.title])
    if args.css:
        cmd.extend(["--user-style-sheet", args.css])
    for extra in args.wkhtmltopdf_arg:
        cmd.append(extra)
    cmd.extend([input_path, output_path])
    return cmd


def convert_with_pandoc(args: argparse.Namespace) -> None:
    cmd = build_pandoc_cmd(args, args.input, args.output)
    run(cmd)


def convert_with_wkhtmltopdf(args: argparse.Namespace) -> None:
    input_path = args.input
    if input_path.lower().endswith(".md"):
        if not find_exe("pandoc"):
            raise SystemExit(
                "wkhtmltopdf requires HTML input. Install pandoc to preconvert Markdown, or provide an .html file."
            )
        with tempfile.TemporaryDirectory() as tmpdir:
            html_path = os.path.join(tmpdir, "_tmp.html")
            cmd = build_pandoc_cmd(args, input_path, html_path)
            run(cmd)
            cmd = build_wkhtmltopdf_cmd(args, html_path, args.output)
            run(cmd)
            return

    cmd = build_wkhtmltopdf_cmd(args, input_path, args.output)
    run(cmd)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert Markdown/HTML to PDF")
    parser.add_argument("--input", required=True, help="Path to .md or .html")
    parser.add_argument("--output", required=True, help="Path to output .pdf")
    parser.add_argument(
        "--engine",
        choices=["auto", "pandoc", "wkhtmltopdf"],
        default="auto",
        help="Conversion engine",
    )
    parser.add_argument("--css", help="Path to CSS file")
    parser.add_argument("--template", help="Pandoc template file")
    parser.add_argument("--pdf-engine", help="Pandoc PDF engine (e.g., weasyprint, xelatex)")
    parser.add_argument("--toc", action="store_true", help="Include table of contents (pandoc only)")
    parser.add_argument("--title", help="Document title")
    parser.add_argument(
        "--metadata",
        action="append",
        default=[],
        help="Pandoc metadata key=value (repeatable)",
    )
    parser.add_argument(
        "--pandoc-arg",
        action="append",
        default=[],
        help="Extra pandoc arg (repeatable)",
    )
    parser.add_argument(
        "--wkhtmltopdf-arg",
        action="append",
        default=[],
        help="Extra wkhtmltopdf arg (repeatable)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.engine == "pandoc":
        if not find_exe("pandoc"):
            raise SystemExit("pandoc not found on PATH")
        convert_with_pandoc(args)
        return

    if args.engine == "wkhtmltopdf":
        if not find_exe("wkhtmltopdf"):
            raise SystemExit("wkhtmltopdf not found on PATH")
        convert_with_wkhtmltopdf(args)
        return

    # auto
    if find_exe("pandoc"):
        convert_with_pandoc(args)
        return
    if find_exe("wkhtmltopdf"):
        convert_with_wkhtmltopdf(args)
        return

    raise SystemExit("No converter found. Install pandoc or wkhtmltopdf and retry.")


if __name__ == "__main__":
    main()