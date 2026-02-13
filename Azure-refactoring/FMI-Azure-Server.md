# FMI Azure Server List

- Source: `Azure-refactoring/FMI-サーバ一覧-202512.xlsx` (sheet: サーバ(202505)), `Azure-refactoring/管理者データ のコピー.xlsx`
- Note: 管理者データは基本情報のみを記載（パスワード/機密備考は除外）

| サーバ名 | 状態 | 機種名 | ロール | 役割 | OS | OSサポート期限 | メモリ | ディスク | ストレージ | IPアドレス | 導入時期 | メーカー保守期限 | サポート先 | Azure監視保守 | 管理グループ | 管理対象機器/サービス | 管理者アカウント | 管理URL | 管理備考 | 管理データシート |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FMISV302 | 稼働中 | Standard A4 v2 | D365 バッチサーバ | D365バッチ処理 | Windows Server 2016 Datacenter | 2027-01-12 | 8GB | 159GB | Standard HDD LRS | 10.10.1.11 | 2019-03-01 |  | FBJ/SCSK | 〇 |  | fmisv302\FMAdmin | FMAdmin / D365bat |  | 記載あり（機密除外） | 現在 |
| FMISV303 | 稼働中 | Standard D2as v4 | WSUS | Windows Update サーバ | Windows Server 2019 Datacenter | 2029-01-09 | 8GB | 127GB | Standard SSD LRS | 10.10.1.12 | 2019-06-01 |  | FBJ | 〇 |  | fmisv303\FMAdmin | FMAdmin |  | 記載あり（機密除外） | 現在 |
| FMISV304 | 稼働中 | Standard D2as v4 | AD#1(FSMO/ADCS/DNS） | ユーザーの認証サーバ | Windows Server 2016 Datacenter | 2027-01-12 | 8GB | 127GB | Standard SSD LRS | 10.10.1.13 | 2019-06-01 |  | FBJ | - |  | fmisv304\FMAdmin | FMAdmin |  | 記載あり（機密除外） | 現在 |
| FMISV306 | 稼働中 | Standard D4 v3 | X-point2.7 | 電子稟議サーバ | Windows Server 2016 Datacenter | 2027-01-12 | 16GB | 240GB | Standard SSD LRS | 10.10.1.15 | 2019-06-01 |  | FBJ | - |  | fmisv306\FMAdmin | FMAdmin |  | 記載あり（機密除外） | 現在 |
| FMISV224 (Azure上: FMISV307) | 稼働中 | Standard D2as v4 | SKYSEA | PC資産管理 | Windows Server 2016 Datacenter | 2027-01-12 | 8GB | 627GB | Standard SSD LRS | 10.10.1.16 | 2019-06-01 |  | FBJ | - |  | fmisv224\FMAdmin | FMAdmin |  | 記載あり（機密除外） | 現在 |
| FMISV309 | 稼働中 | Standard D2as v4 | SKYSEA HTTP-GW | PC資産管理外部接続用サーバ | Windows Server 2016 Datacenter | 2027-01-12 | 8GB | 127GB | Standard SSD LRS | 10.10.254.10 | 2019-06-01 |  | FBJ | - |  | fmisv309\FMAdmin | FMAdmin |  | 記載あり（機密除外） | 現在 |
| FMISV323 | 稼働中 | Standard D2as v4 | AAD Connect | Office365・IntuneConnect同期サーバ | Windows Server 2019 Datacenter | 2029-01-09 | 8GB | 127GB | Standard SSD LRS | 10.10.1.4 | 2023-06-01 |  | FBJ | - |  | fmisv323\fmadmin | fmadmin |  | 記載あり（機密除外） | 現在 |
| FMISV324 | 稼働中 | Standard DS11 v2 | 勘定奉行V11ERP | 財務会計サーバ | Windows Server 2019 Datacenter | 2029-01-09 | 14GB | 127GB/40GB | Standard SSD LRS | 10.10.1.5 | 2023-08-01 |  | FBJ | △（検討中） |  | fmisv324\fmadmin | fmadmin |  | 記載あり（機密除外） | 現在 |
| FMISV105 | 稼働中 | Standard D4s v3 | ファイルサーバ | 共有フォルダを格納 | Windows Server 2019 Datacenter | 2029-01-09 | 16GB | 18TB＋8TB | Standard HDD LRS | 10.10.1.19 | 2023/6月 |  | FBJ | 〇 |  | fmisv105\administrator | administrator |  | 記載あり（機密除外） | 現在 |
| FCISV101 | 稼働中 | Standard D2s v3 | FCI用ファイルサーバ | 共有フォルダを格納 | Windows Server 2019 Datacenter | 2029-01-09 | 8GB | 2TB | Standard HDD LRS | 10.10.2.10 | 2022-08-01 |  | FBJ | 〇 |  |  |  |  |  |  |
