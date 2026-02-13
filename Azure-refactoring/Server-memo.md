# Server Memo

Azureサーバーごとのメモ用テンプレート。追記後にマージしやすいよう1台ずつ分割。

## サマリー

| サーバ名 | ロール | サポート期間 | メモ欄コメント |
| --- | --- | --- | --- |
| FMISV302 | D365 バッチサーバ | 2027-01-12 | 異動対象 / 低 / アプリ移行inhouse |
| FMISV303 | WSUS | 2029-01-09 | 対象外 |
| FMISV304 | AD#1(FSMO/ADCS/DNS） | 2027-01-12 | 対象 / softbank移行サポート / 最初に移行 |
| FMISV306 | X-point2.7 | 2027-01-12 | 対象外 |
| FMISV224 (Azure上: FMISV307) | SKYSEA | 2027-01-12 | 対象 / ADの次に移行 / Skyseaサポート必要、Softbakにコーディネートを要請 / 移行時に現時点の設定のエクスポートしてほしいと要請 |
| FMISV309 | SKYSEA HTTP-GW | 2027-01-12 | ADの次に移行 / Skyseaサポート必要、Softbakにコーディネートを要請 / 移行時に現時点の設定のエクスポートしてほしいと要請 |
| FMISV323 | AAD Connect | 2029-01-09 | 対象外 |
| FMISV324 | 勘定奉行V11ERP | 2029-01-09 | 対象外 |
| FMISV105 | ファイルサーバ | 2029-01-09 | 対象外 |
| FCISV101 | FCI用ファイルサーバ | 2029-01-09 | 対象外ー＞SPOへの移行を検討 |

## FMISV302
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FMISV302
  - IPアドレス: 10.10.1.11
  - OS: Windows Server 2016 Datacenter
  - OSサポート期限: 2027-01-12

- 構成
  - 機種名: Standard A4 v2
  - ロール: D365 バッチサーバ
  - 役割: D365バッチ処理
  - メモリ: 8GB
  - ディスク: 159GB
  - ストレージ: Standard HDD LRS
  - 導入時期: 2019-03-01
  - メーカー保守期限: 
  - サポート先: FBJ/SCSK
  - Azure監視保守: 〇

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
- 異動対象
- 低
- Softbakアプリ移動対象外（Inhouse）
- 
- 

## FMISV303
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FMISV303
  - IPアドレス: 10.10.1.12
  - OS: Windows Server 2019 Datacenter
  - OSサポート期限: 2029-01-09

- 構成
  - 機種名: Standard D2as v4
  - ロール: WSUS
  - 役割: Windows Update サーバ
  - メモリ: 8GB
  - ディスク: 127GB
  - ストレージ: Standard SSD LRS
  - 導入時期: 2019-06-01
  - メーカー保守期限: 
  - サポート先: FBJ
  - Azure監視保守: 〇

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
  - 対象外

## FMISV304
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FMISV304
  - IPアドレス: 10.10.1.13
  - OS: Windows Server 2016 Datacenter
  - OSサポート期限: 2027-01-12

- 構成
  - 機種名: Standard D2as v4
  - ロール: AD#1(FSMO/ADCS/DNS）
  - 役割: ユーザーの認証サーバ
  - メモリ: 8GB
  - ディスク: 127GB
  - ストレージ: Standard SSD LRS
  - 導入時期: 2019-06-01
  - メーカー保守期限: 
  - サポート先: FBJ
  - Azure監視保守: -

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
  - 対象
  - softbank移行サポート
  - 最初に移行

## FMISV306
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FMISV306
  - IPアドレス: 10.10.1.15
  - OS: Windows Server 2016 Datacenter
  - OSサポート期限: 2027-01-12

- 構成
  - 機種名: Standard D4 v3
  - ロール: X-point2.7
  - 役割: 電子稟議サーバ
  - メモリ: 16GB
  - ディスク: 240GB
  - ストレージ: Standard SSD LRS
  - 導入時期: 2019-06-01
  - メーカー保守期限: 
  - サポート先: FBJ
  - Azure監視保守: -

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
  - 対象外

## FMISV224 (Azure上: FMISV307)
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FMISV224 (Azure上: FMISV307)
  - IPアドレス: 10.10.1.16
  - OS: Windows Server 2016 Datacenter
  - OSサポート期限: 2027-01-12

- 構成
  - 機種名: Standard D2as v4
  - ロール: SKYSEA
  - 役割: PC資産管理
  - メモリ: 8GB
  - ディスク: 627GB
  - ストレージ: Standard SSD LRS
  - 導入時期: 2019-06-01
  - メーカー保守期限: 
  - サポート先: FBJ
  - Azure監視保守: -

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
  - 対象
  - ADの次に移行
  - Skyseaサポート必要、Softbakにコーディネートを要請
  - 移行時に現時点の設定のエクスポートしてほしいと要請
  - 

## FMISV309
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FMISV309
  - IPアドレス: 10.10.254.10
  - OS: Windows Server 2016 Datacenter
  - OSサポート期限: 2027-01-12

- 構成
  - 機種名: Standard D2as v4
  - ロール: SKYSEA HTTP-GW
  - 役割: PC資産管理外部接続用サーバ
  - メモリ: 8GB
  - ディスク: 127GB
  - ストレージ: Standard SSD LRS
  - 導入時期: 2019-06-01
  - メーカー保守期限: 
  - サポート先: FBJ
  - Azure監視保守: -

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
  - ADの次に移行
  - Skyseaサポート必要、Softbakにコーディネートを要請
  - 移行時に現時点の設定のエクスポートしてほしいと要請

## FMISV323
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FMISV323
  - IPアドレス: 10.10.1.4
  - OS: Windows Server 2019 Datacenter
  - OSサポート期限: 2029-01-09

- 構成
  - 機種名: Standard D2as v4
  - ロール: AAD Connect
  - 役割: Office365・IntuneConnect同期サーバ
  - メモリ: 8GB
  - ディスク: 127GB
  - ストレージ: Standard SSD LRS
  - 導入時期: 2023-06-01
  - メーカー保守期限: 
  - サポート先: FBJ
  - Azure監視保守: -

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
  - 対象外

## FMISV324
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FMISV324
  - IPアドレス: 10.10.1.5
  - OS: Windows Server 2019 Datacenter
  - OSサポート期限: 2029-01-09

- 構成
  - 機種名: Standard DS11 v2
  - ロール: 勘定奉行V11ERP
  - 役割: 財務会計サーバ
  - メモリ: 14GB
  - ディスク: 127GB/40GB
  - ストレージ: Standard SSD LRS
  - 導入時期: 2023-08-01
  - メーカー保守期限: 
  - サポート先: FBJ
  - Azure監視保守: △（検討中）

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
  - 対象外

## FMISV105
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FMISV105
  - IPアドレス: 10.10.1.19
  - OS: Windows Server 2019 Datacenter
  - OSサポート期限: 2029-01-09

- 構成
  - 機種名: Standard D4s v3
  - ロール: ファイルサーバ
  - 役割: 共有フォルダを格納
  - メモリ: 16GB
  - ディスク: 18TB＋8TB
  - ストレージ: Standard HDD LRS
  - 導入時期: 2023/6月
  - メーカー保守期限: 
  - サポート先: FBJ
  - Azure監視保守: 〇

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
  - 対象外

## FCISV101
- サーバ情報
  - 状態: 稼働中
  - 設置場所: Azure
  - サーバ名: FCISV101
  - IPアドレス: 10.10.2.10
  - OS: Windows Server 2019 Datacenter
  - OSサポート期限: 2029-01-09

- 構成
  - 機種名: Standard D2s v3
  - ロール: FCI用ファイルサーバ
  - 役割: 共有フォルダを格納
  - メモリ: 8GB
  - ディスク: 2TB
  - ストレージ: Standard HDD LRS
  - 導入時期: 2022-08-01
  - メーカー保守期限: 
  - サポート先: FBJ
  - Azure監視保守: 〇

- メモ欄
  - [ ] 変更予定
  - [ ] 課題
  - [ ] 対応履歴
  - 自由記入:
  - 対象外ー＞SPOへの移行を検討


InterfaceCAT
  - 移行時に現時点の設定のエクスポートしてほしいと要請
