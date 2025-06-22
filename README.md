# conspro2

建機サービス管理システム開発用のレポジトリです。

## システム概要
建設機械の販売・レンタル・修理業務を一元管理するDjangoベースのWebアプリケーションです。
- 在庫管理、作業（修理）管理、レンタル管理、顧客・会社・メーカー管理、帳票出力などをサポートします。

## 主な機能
- **在庫管理**：建機の在庫情報、状態、整備状況、履歴管理
- **作業管理**：修理・整備等の作業案件、明細、進捗管理
- **レンタル管理**：レンタル注文、期間、顧客、明細管理
- **顧客・会社・メーカー管理**：各種マスタ管理
- **帳票出力**：注文書・請求書・見積書等のダウンロード
- **認証機能**：ログイン・ログアウト

## モデル構成（主要モデル）
- `Company`：会社情報
- `Client`：顧客情報
- `Maker`：メーカー情報
- `Type_Machine`：機械分類
- `Inventory`：在庫（建機）情報
- `InventoryOrderRow`：在庫注文明細
- `Work`：作業（修理・整備）案件
- `WorkRow`：作業明細
- `RentalOrder`：レンタル注文
- `RentalOrderRow`：レンタル注文明細
- `Notice`：お知らせ

## 主な画面・URL
- `/conspro2/login/`：ログイン画面
- `/conspro2/inventory/`：在庫一覧・検索
- `/conspro2/work/`：作業一覧・検索
- `/conspro2/rental_order/`：レンタル注文一覧・検索
- `/admin/`：管理画面

## 開発環境構築
### コンテナ起動
```sh
docker compose build
docker compose up -d
# 初回のみ
docker exec -it conspro2 bash
python manage.py migrate
python manage.py createsuperuser
```
### modelクラス追加後のマイグレーション実行
```sh
python manage.py makemigrations main
python manage.py sqlmigrate main XXXX
python manage.py migrate
python manage.py showmigrations
```
### その他
```sh
docker exec -it conspro2 bash
docker logs -f conspro2
```

### バッチ
```sh
python manage.py inventory_close
```

### 画面起動
https://localhost:3443/  
https://localhost:3443/admin/  
https://localhost:3443/conspro2/login/  

---

## 必要要件
- Python, Django, MySQL
- 依存パッケージは `requirements.txt` を参照

## ライセンス
このリポジトリはMITライセンスです。





