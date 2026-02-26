# Azure OpenAI リソース構築スクリプト（テンプレート）
# 事前条件: Azure CLI ログイン済み (`az login`)
# 使い方: 変数を埋めて実行

param(
  [string]$SubscriptionId = "",
  [string]$ResourceGroup = "rg-fmi-openai",
  [string]$Location = "japaneast",
  [string]$AccountName = "fmi-openai",
  [string]$DeploymentName = "policy-extract",
  [string]$ModelName = "gpt-4o-mini",
  [string]$ModelVersion = "2024-07-18",
  [string]$SkuName = "S0"
)

if ($SubscriptionId -ne "") {
  az account set --subscription $SubscriptionId | Out-Null
}

Write-Host "[1/4] Resource Group 作成/確認"
az group create --name $ResourceGroup --location $Location | Out-Null

Write-Host "[2/4] Azure OpenAI アカウント作成/確認"
# 既存なら作成をスキップ
$exists = az cognitiveservices account show --name $AccountName --resource-group $ResourceGroup --query "name" -o tsv 2>$null
if (-not $exists) {
  az cognitiveservices account create \
    --name $AccountName \
    --resource-group $ResourceGroup \
    --location $Location \
    --kind OpenAI \
    --sku $SkuName \
    --yes | Out-Null
}

Write-Host "[3/4] モデルデプロイ作成/確認"
# 既存デプロイ確認
$depExists = az cognitiveservices account deployment show \
  --name $AccountName \
  --resource-group $ResourceGroup \
  --deployment-name $DeploymentName \
  --query "name" -o tsv 2>$null

if (-not $depExists) {
  az cognitiveservices account deployment create \
    --name $AccountName \
    --resource-group $ResourceGroup \
    --deployment-name $DeploymentName \
    --model-name $ModelName \
    --model-version $ModelVersion \
    --model-format OpenAI | Out-Null
}

Write-Host "[4/4] エンドポイント/キーの取得"
$endpoint = az cognitiveservices account show --name $AccountName --resource-group $ResourceGroup --query "properties.endpoint" -o tsv
$apiKey = az cognitiveservices account keys list --name $AccountName --resource-group $ResourceGroup --query "key1" -o tsv

Write-Host "AZURE_OPENAI_ENDPOINT=$endpoint"
Write-Host "AZURE_OPENAI_API_KEY=$apiKey"
Write-Host "AZURE_OPENAI_DEPLOYMENT=$DeploymentName"
Write-Host "AZURE_OPENAI_API_VERSION=2024-06-01"
