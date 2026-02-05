import argparse
import json
import re
from pathlib import Path

import pdfplumber


def normalize_date(s: str):
    m = re.search(r"(\d{4})年\s*(\d{1,2})月\s*(\d{1,2})日", s)
    if not m:
        return None
    y, mo, d = m.groups()
    return f"{y}-{int(mo):02d}-{int(d):02d}"


def extract_text(pdf_path: Path) -> str:
    text = []
    with pdfplumber.open(pdf_path) as p:
        for page in p.pages:
            t = page.extract_text() or ""
            text.append(t)
    return "\n".join(text)


def extract_fields(full: str, pdf_path: Path, doc_id: str):
    # Title
    m_title = re.search(r"^(.*?規程)\s*$", full, flags=re.MULTILINE)
    title = m_title.group(1).strip() if m_title else ""

    # Appendix / revision history
    appendix_block = ""
    if "附 則" in full:
        appendix_block = full.split("附 則", 1)[1]

    revision_history = []
    for line in appendix_block.splitlines():
        if "施行" in line or "更新" in line:
            date = normalize_date(line)
            if date:
                revision_history.append({
                    "date": date,
                    "type": "改正施行" if "改正" in line else ("更新" if "更新" in line else "施行"),
                    "note": line.strip(),
                })

    effective_dates = [r["date"] for r in revision_history if r["type"] in ("施行", "改正施行")]
    if effective_dates:
        effective_dates = [effective_dates[0]]

    # Scope assets (第2条)
    scope_assets = []
    m = re.search(r"第2条[\s\S]*?第3条", full)
    if m:
        block = m.group(0)
        items = re.split(r"、", block)
        for it in items:
            it = it.strip()
            if any(k in it for k in [
                "サーバー", "ネットワーク", "パソコン", "周辺", "記録媒体",
                "通信機器", "ミドルウェア", "オペレーティングシステム",
                "ソフトウェア", "データベース"
            ]):
                it = re.sub(r"\(.*?\)", "", it)
                it = it.replace("（以下、総称して「情報システム機器類」という。）", "")
                scope_assets.append(it)
    scope_assets = list(dict.fromkeys(scope_assets))

    # Roles (第3〜5条)
    roles = []
    if re.search(r"情報システム管理責任者", full):
        roles.append({"role": "情報システム管理責任者", "assigned_to": "コーポレート推進部長"})
    if re.search(r"情報システム担当者", full):
        roles.append({"role": "情報システム担当者", "assigned_by": "情報システム管理責任者"})

    # Responsibilities (第4条)
    responsibilities = []
    m = re.search(r"第4条[\s\S]*?第5条", full)
    if m:
        block = m.group(0)
        for item in re.findall(r"\(\d+\)\s*([^\n]+)", block):
            responsibilities.append(item.strip())

    # Prohibitions (第8条)
    prohibitions = []
    m = re.search(r"第8条[\s\S]*?第9条", full)
    if m:
        block = m.group(0)
        for item in re.findall(r"（\d+）\s*([^\n]+)", block):
            prohibitions.append(item.strip())

    # Reporting triggers (第9条)
    reporting_triggers = []
    m = re.search(r"第9条[\s\S]*?第10条", full)
    if m:
        block = m.group(0)
        for item in re.findall(r"（\d+）\s*([^\n]+)", block):
            reporting_triggers.append(item.strip())

    # Required actions (第10条)
    required_actions = []
    m = re.search(r"第10条[\s\S]*?第11条", full)
    if m:
        block = m.group(0)
        for line in block.splitlines():
            if "しなければならない" in line or "できる" in line:
                required_actions.append(line.strip())

    return {
        "doc_id": doc_id,
        "title": title,
        "doc_type": "規程",
        "effective_dates": effective_dates,
        "revision_history": revision_history,
        "scope_assets": scope_assets,
        "roles": roles,
        "responsibilities": responsibilities,
        "prohibitions": prohibitions,
        "reporting_triggers": reporting_triggers,
        "required_actions": required_actions,
        "evidence_links": [str(pdf_path)],
    }


def main():
    ap = argparse.ArgumentParser(description="Read-only extraction from regulation PDF.")
    ap.add_argument("--input", required=True, help="Path to input PDF")
    ap.add_argument("--output", required=True, help="Path to output JSON")
    ap.add_argument("--doc-id", required=True, help="Document ID (e.g., 07-0120)")
    args = ap.parse_args()

    pdf_path = Path(args.input)
    out_path = Path(args.output)

    full = extract_text(pdf_path)
    data = extract_fields(full, pdf_path, args.doc_id)

    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
