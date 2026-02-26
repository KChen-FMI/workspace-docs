# ServiceNow定義をベースにしたFMI向けITサービスカタログ紹介資料（PPT構成ドラフト）

> 出典: `run-book/it-service-catalogue/IT サービスカタログとは？ - ServiceNow.pdf`  
> 目的: ServiceNowの定義をFMI ITに適用するための共通理解をつくる

---

## Slide 1. タイトル

**ServiceNowのサービスカタログ定義をFMI ITへ適用する**  
FMI ITサービスカタログ導入の考え方と実装イメージ

- 対象: IT部門、部門IT担当、業務オーナー
- ゴール: 「何を載せるか」「どう運用するか」「どう改善するか」を合意する

---

## Slide 2. なぜ今サービスカタログか

- 依頼窓口が分散し、対応品質・速度がばらつく
- 依頼内容の定義が曖昧で、手戻りが多い
- 対応状況が見えず、利用者体験が低下しやすい

**ServiceNow定義の要点**
- サービスカタログは「社内で利用できるITリソースのデータベース」
- 利用者ニーズに効率的・効果的に応える設計が必要

---

## Slide 3. サービスカタログの定義（ServiceNow）

```mermaid
flowchart LR
    A[利用者ニーズ] --> B[ITサービスカタログ: 利用可能サービスのDB]
    B --> C[標準化された申請]
    C --> D[履行・提供]
    D --> E[進捗可視化]
    E --> F[満足度向上・運用改善]
```

- カタログは「メニュー」であり、申請の入口を標準化する
- サービス、条件、SLA、コストなどを明示する

---

## Slide 4. サービスカタログとセルフサービスポータルの違い

```mermaid
%%{init: {"themeVariables":{"fontSize":"8px"},"flowchart":{"nodeSpacing":15,"rankSpacing":20,"padding":4}}}%%
flowchart TB
    subgraph Catalog[ITサービスカタログ];
      C1[提供可能サービス];
      C2[説明・条件・SLA・コスト];
      C3[オーナー・可用性];
    end;

    subgraph Portal[セルフサービスポータル];
      P1[検索/ナビゲーション];
      P2[申請フォーム];
      P3[チケット起票];
      P4[進捗確認・通知];
    end;

    Catalog --> Portal;
```

- カタログ: 「何が頼めるか」の定義
- ポータル: 「どう頼むか」のUI
- 実運用では両者を統合して提供する

---

## Slide 5. ServiceNowが示す主なメリット

```mermaid
%%{init: {"themeVariables":{"fontSize":"12px"}}}%%
mindmap
  root((ITサービスカタログの価値))
    セルフサービス強化
    運用効率向上
    使いやすさ最適化
    生産性向上
    可視性向上
    満足度向上
```

- 利用者: 必要サービスを自力で特定しやすい
- IT部門: 定型処理を標準化・自動化しやすい
- 管理者: 指標に基づく改善判断がしやすい

---

## Slide 6. カタログに含めるべき情報（ServiceNow準拠）

```mermaid
%%{init: {"themeVariables":{"fontSize":"12px"}}}%%
classDiagram
  class ServiceItem {
    +サービス名
    +カテゴリ
    +説明
    +オーナー
    +可用性
    +SLA
    +コスト
  }

  class RequestForm {
    +申請者
    +対象ユーザー
    +希望期限
    +業務影響
    +添付
  }

  ServiceItem <.. RequestForm : 参照して申請
```

- 最低限、上記7項目は全サービスで統一管理する
- 申請フォームは必要最小限で設計する

---

## Slide 7. 含めるべきでない情報

```mermaid
flowchart LR
    A[カタログ掲載候補] --> B{利用者に必要?}
    B -- Yes --> C[掲載]
    B -- No --> D[非掲載]
    D --> D1[機密情報]
    D --> D2[管理者のみ必要な内部実装]
    D --> D3[対象外ユーザー向け情報]
```

- 機密情報や不要な詳細は除外する
- 対象ユーザーに応じてサービスを絞る
- 「選択疲れ」を防ぐ

---

## Slide 8. ServiceNow流の構築ステップ

```mermaid
flowchart LR
    S1[1. 利害関係者を集める] -->
    S2[2. ユーザー/履行責任を特定] -->
    S3[3. サービス棚卸と定義] -->
    S4[4. 分類/タグ付け/バンドル] -->
    S5[5. カタログ設計] -->
    S6[6. テストと展開] -->
    S7[7. 継続改善]
```

- まず目的と利用者を定義する
- 展開後もKPIで継続的に改善する

---

## Slide 9. FMI適用時の業務フロー（To-Be）

```mermaid
sequenceDiagram
    participant U as 利用者
    participant P as ポータル
    participant C as サービスカタログ
    participant A as 承認者
    participant F as 履行担当(IT)

    U->>P: サービス検索/選択
    P->>C: 定義・条件・SLA参照
    U->>P: 申請送信
    P->>A: 承認依頼
    A-->>P: 承認/却下
    P->>F: 承認済み依頼を連携
    F-->>P: 対応状況更新
    P-->>U: ステータス通知/完了
```

- 申請から完了通知までを一気通貫で見える化
- 承認・履行責任を明確化

---

## Slide 10. FMIで最初に定義すべきサービス領域

```mermaid
flowchart TB
    R[優先導入領域] --> R1[ID/アクセス: M365・権限]
    R --> R2[端末: PC・モバイル]
    R --> R3[コラボ: Teams・ML]
    R --> R4[ネットワーク: VPN]
    R --> R5[セキュリティ通報]
    R --> R6[入退社ライフサイクル]
```

- 申請件数が多く標準化効果が大きい領域から開始
- まず10〜15サービスに絞って品質を安定化

---

## Slide 11. 導入ロードマップ（90日）

```mermaid
gantt
    title FMI ITサービスカタログ立上げ（90日）
    dateFormat  YYYY-MM-DD
    section 設計
    スコープ/体制合意           :a1, 2026-03-01, 14d
    サービス定義（10〜15件）     :a2, after a1, 21d
    section 実装
    ポータル/フォーム実装         :b1, after a2, 21d
    通知・承認フロー実装          :b2, after a2, 21d
    section 展開
    UAT/部門テスト               :c1, after b1, 14d
    本番リリース/周知             :c2, after c1, 7d
    section 改善
    KPIレビュー初回              :d1, after c2, 14d
```

- 3か月で最小実用版（MVP）を公開
- 以降は四半期ごとに追加拡張

---

## Slide 12. 成功指標（KPI）

- SLA遵守率
- 初回解決率（FCR）
- 申請リードタイム
- 再申請率（フォーム不備）
- CSAT（利用者満足度）

```mermaid
flowchart LR
    K1[SLA遵守率] --> G[サービス品質]
    K2[FCR] --> G
    K3[リードタイム] --> G
    K4[再申請率] --> G
    K5[CSAT] --> G
    G --> M[四半期改善アクション]
```

---

## Slide 13. 付録: FMI版サービス項目（初期案）

- PC初期セットアップ
- M365アカウント発行/変更
- 共有フォルダ権限付与
- ソフトウェア導入申請
- VPN設定
- Teams会議トラブル対応
- セキュリティインシデント報告
- 入社/異動/退職の一括IT手配

詳細は `run-book/it-service-catalogue/service-catalogue-onapage.md` を参照。

---

## Slide 14. 参考情報

- `run-book/it-service-catalogue/IT サービスカタログとは？ - ServiceNow.pdf`
- `run-book/it-service-catalogue/service-catalogue-onapage.md`

