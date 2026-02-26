# LLM抽出プロンプト設計（叩き台）

## 目的
- PDF本文から `schema.md` に準拠したJSONを抽出する
- 推測を避け、人間レビューしやすい出力にする
- 追加で「期待された目的（期待されたOutput）」「対象者」「スコープ」を含める

## 入力（想定）
- `doc_id`
- `file_path`
- `raw_text`（PDF抽出テキスト）

## 出力（必須）
- JSONのみを返す
- `schema.md` のフィールドをすべて含める
- 不明な場合は空配列/空文字にする
- `reviewer_notes` は空文字
- `evidence_links` に `file_path` を1件入れる
- 追加フィールドを含める
  - `expected_output`（期待された目的）
  - `target_audience`（対象者）
  - `scope`（スコープ）

## システム指示（案）
```
あなたはITのサービスカタログを管理する担当者であり、規程・方針文書のから、ITサービスに必要な情報を指定スキーマに沿ってJSONを生成してください。  
推測で補完せず、本文に明示された内容のみを記載してください。
出力はJSONのみ。日本語のまま記載する。
以下の情報も追加してください。
最後に期待された目的（期待されたOutput）
対象者
スコープ
```

## ユーザープロンプト（案）
```
以下の情報からJSONを生成してください。

[doc_id]
{doc_id}

[file_path]
{file_path}

[raw_text]
{raw_text}

[output_schema]
{
  "doc_id": "",
  "title": "",
  "doc_type": "規程",
  "effective_dates": ["YYYY-MM-DD"],
  "revision_history": [
    {"date": "YYYY-MM-DD", "type": "施行|改正施行|更新", "note": ""}
  ],
  "scope_assets": [],
  "roles": [
    {"role": "", "assigned_to": ""},
    {"role": "", "assigned_by": ""}
  ],
  "responsibilities": [],
  "prohibitions": [],
  "reporting_triggers": [],
  "required_actions": [],
  "reviewer_notes": "",
  "evidence_links": [],
  "expected_output": "",
  "target_audience": "",
  "scope": ""
}

[constraints]
- 出力はJSONのみ
- 推測で補完しない（本文で確認できない情報は空）
- 日本語のまま記載
- `doc_id` は入力値を使用
- `evidence_links` に `file_path` を入れる
- `expected_output` / `target_audience` / `scope` は本文に明示がある場合のみ記入し、なければ空文字
```

## 抽出ルールの指針（LLM向け）
- `title`: 文書タイトル（冒頭の見出し）
- `doc_type`: 通常は「規程」/「方針」/「計画書」など本文表現に合わせる
- `effective_dates`: 施行日があれば最初の1件
- `revision_history`: 附則や改定履歴の行
- `scope_assets`: 情報資産/機器/データ等の明示がある場合
- `roles`: 役割名と任命主体/任命先
- `responsibilities`: 「〜する」「〜を遵守」等の義務・責務
- `prohibitions`: 「〜してはならない」等の禁止
- `reporting_triggers`: 「報告」「連絡」「届出」などの条件
- `required_actions`: 明確な必須行動
- `expected_output`: 文書の期待成果・目的が明示されている場合
- `target_audience`: 対象者/適用対象/想定ユーザーが明示されている場合
- `scope`: 対象範囲/適用範囲が明示されている場合

## TODO（確定が必要）
- モデル/温度/最大トークン
- 長文時の分割方針
- 返却JSONの検証方法
