# testsite
掲示板を作成

# 機能
スレッド作成  
メッセージ投稿 

# 環境
docker 20.10.9  
docker-compose 1.25.0  
python 3.8 (Dockerfile)  
postgres:latest (docker-compose.yml)  
nginx:latest (docker-compose.yml)  
Django 3.0.4 (requirements.txt)  
psycopg2 2.8.4 (requirements.txt)  
uwsgi 2.0.18 (requirements.txt)  

# 起動
「docker-compose.yml」があるディレクトリで「docker-compose up」  

# マイグレーション
docker-compose run django ./manage.py makemigrations testsite  
docker-compose run django ./manage.py migrate