# conspro2

建機管理システム開発用のレポジトリです

# 開発環境構築
## コンテナ起動
```sh
docker-compose build
docker-compose up -d
# 初回にやる
docker exec -it conspro2-web bash
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
docker exec -it conspro2-web bash
docker logs -f conspro2-web
```
## 画面起動
https://localhost:3443/  
https://localhost:3443/admin/  
https://localhost:3443/conspro2/login/  

Username:	dyq95yimdrocta60h5f4
Password:	pscale_pw_4xErkQMyhr6gWlCaW4H2eP15x2Qtnt27noDoRxQ8Ulp




