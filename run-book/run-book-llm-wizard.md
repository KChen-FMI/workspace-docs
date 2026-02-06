# 業務カタログ自動更新構想 --OnePager--

## 目的
- 業務カタログを **最低限のマニュアルワーク** で維持する
- 設計の美しさより **運用が回り続けること** を最優先する
- **人間は決断と責任**、機械（LLM）は分析と整理を担う

---

## 基本思想
> 人間は決める  
> LLM は材料を揃える

- LLM は **判断・更新を行わない**
- Wizard は **差分と影響を可視化する**
- 業務カタログは **1サービス＝1行（Single Source of Truth）** を維持する
- 多テーブル正規化は初期段階では行わない

---

## 全体フロー（Mermaid）

```mermaid
flowchart LR
  subgraph DS[データソース]
    R1[社内規程 PDF]
    R2[定例WF / 稟議 Onepage]
    R3[JIRA チケット]
    R4[インシデント（JIRA）]
    R5[単発プロジェクト]
  end

  subgraph IN[Intake（投入箱）]
    F1[所定フォルダ / フォーム]
    IR[Intake レコード（1行）]
  end

  subgraph AI[LLM 分析]
    EX[要約・属性抽出\\n候補サービス提示\\n根拠抽出]
    JR[LLM 結果 JSON\\n（証跡）]
  end

  subgraph WZ[Wizard]
    CAND[既存サービス候補\\n最大3件]
    DIFF[差分（diff）表示]
    DEC{新規 or 更新}
  end

  subgraph SC[サービスカタログ]
    SV[サービス（1行）]
    EV[根拠リンク]
  end

  R1 --> F1 --> IR --> EX --> JR --> CAND --> DIFF --> DEC
  R2 --> F1
  R3 --> F1
  R4 --> F1
  R5 --> F1

  DEC --> SV
  JR -.参照.-> EV
  EV -.リンク.-> SV
```
