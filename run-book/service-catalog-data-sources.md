# Service Catalog DB: Data Sources (Draft)

This file captures how each Service can link to data sources. The relationship is **0..many** from Service to each data source type (a Service may have none).

## Flowchart (Service Catalog → Service → Activities + Data Sources)

```mermaid
flowchart LR
  subgraph DS[データソース]
    R1[社内規程]
    R2[定例ワークフロー]
    R3[JIRAチケット]
    R4[インシデント（JIRA）]
    R5[単発プロジェクト]
  end

  subgraph SC[サービスカタログ]
    SV[サービス]:::service -->|1..多| AC[アクティビティ]
  end

  R1 -. "0..多" .-> SV
  R2 -. "0..多" .-> SV
  R3 -. "0..多" .-> SV
  R4 -. "0..多" .-> SV
  R5 -. "0..多" .-> SV

  classDef service fill:#eef3ff,stroke:#556,stroke-width:1px;
```
