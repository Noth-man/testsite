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

# 画面
ホーム  
![image](https://user-images.githubusercontent.com/54675731/143544694-5e4d4908-56ec-429e-8b0d-662f7bc9dcd1.png)  
スレッド  
![image](https://user-images.githubusercontent.com/54675731/143544713-321bd3f4-1482-4745-a048-f1e6b6327813.png)  
スレッド作成
![image](https://user-images.githubusercontent.com/54675731/143544737-40f1ad64-681c-4755-ac3a-2b2ef7614476.png)