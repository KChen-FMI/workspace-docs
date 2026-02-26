# LLM抽出 実行手順（Azure OpenAI）

## 必要な環境変数
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_DEPLOYMENT`
- `AZURE_OPENAI_API_VERSION`（任意、既定: `2024-06-01`）

## 前提
- `run-book/POC/llm-extraction-prompt-draft.md` が存在する
- PDF本文は事前にテキスト化して入力する（例: pdfplumber）

## 例: 1件実行
```powershell
$env:AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE.openai.azure.com"
$env:AZURE_OPENAI_API_KEY="YOUR_KEY"
$env:AZURE_OPENAI_DEPLOYMENT="YOUR_DEPLOYMENT"
$env:AZURE_OPENAI_API_VERSION="2024-06-01"

python run-book/POC/llm_extract_azure_openai.py \
  --input run-book/POC/Testdata/03-0130_在宅勤務規程_20251001改正.txt \
  --doc-id 03-0130 \
  --file-path "C:\\...\\03-0130_在宅勤務規程_20251001改正.pdf" \
  --prompt run-book/POC/llm-extraction-prompt-draft.md \
  --output run-book/POC/Testdata/03-0130_在宅勤務規程_20251001改正.llm.extracted.json
```

## 注意
- 出力はJSONのみを期待（非JSON混入時は失敗）
- 失敗時は再実行、またはプロンプト調整
