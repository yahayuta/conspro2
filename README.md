# conspro2

建機サービス管理システム開発用のレポジトリです
販売・レンタル・修理義務を管理できます

# 開発環境構築
## コンテナ起動
```sh
docker compose build
docker compose up -d
# 初回にやる
docker exec -it conspro2 bash
python manage.py migrate
python manage.py createsuperuser
```
## modelクラス追加後のマイグレーション実行
```sh
python manage.py makemigrations main
python manage.py sqlmigrate main XXXX
python manage.py migrate
python manage.py showmigrations
```
## その他
```sh
docker exec -it conspro2 bash
docker logs -f conspro2
```

## バッチ
```sh
python manage.py inventory_close
```

## 画面起動
https://localhost:3443/  
https://localhost:3443/admin/  
https://localhost:3443/conspro2/login/  





