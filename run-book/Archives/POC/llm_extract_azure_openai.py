#!/usr/bin/env python
"""
LLM extraction runner (Azure OpenAI).
Reads a prompt draft, fills placeholders, calls Azure OpenAI Chat Completions,
and writes JSON output to *.llm.extracted.json.
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

import requests


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_json(text: str) -> str:
    # Prefer a JSON object from the first '{' to the last '}'
    m = re.search(r"\{[\s\S]*\}", text)
    if not m:
        raise ValueError("No JSON object found in response.")
    return m.group(0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Path to input PDF text (txt).")
    ap.add_argument("--doc-id", required=True, help="Document ID.")
    ap.add_argument("--file-path", required=True, help="Original PDF path.")
    ap.add_argument("--prompt", required=True, help="Prompt draft markdown path.")
    ap.add_argument("--output", required=True, help="Path to output JSON.")
    args = ap.parse_args()

    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "").rstrip("/")
    api_key = os.getenv("AZURE_OPENAI_API_KEY", "")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-06-01")

    if not endpoint or not api_key or not deployment:
        print("Missing Azure OpenAI env vars: AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, AZURE_OPENAI_DEPLOYMENT", file=sys.stderr)
        sys.exit(1)

    raw_text = load_text(Path(args.input))
    prompt_md = load_text(Path(args.prompt))

    # Extract system/user prompt blocks from the draft
    system_match = re.search(r"## システム指示（案）\n```\n([\s\S]*?)\n```", prompt_md)
    user_match = re.search(r"## ユーザープロンプト（案）\n```\n([\s\S]*?)\n```", prompt_md)
    if not system_match or not user_match:
        print("Prompt draft missing system/user blocks.", file=sys.stderr)
        sys.exit(1)

    system_prompt = system_match.group(1)
    user_prompt = user_match.group(1)

    user_prompt = user_prompt.format(
        doc_id=args.doc_id,
        file_path=args.file_path,
        raw_text=raw_text,
    )

    url = f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version={api_version}"
    payload = {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0,
        "max_tokens": 2000,
    }

    resp = requests.post(url, headers={"api-key": api_key, "Content-Type": "application/json"}, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    content = data["choices"][0]["message"]["content"]

    json_text = extract_json(content)
    parsed = json.loads(json_text)

    Path(args.output).write_text(json.dumps(parsed, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
