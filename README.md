# note
note で作っていってるアプリのレポジトリ
試したい時は、以下のコマンドを実行してください。
python manage.py dbshell
psql -U postgres
CREATE DATABASE app;
CREATE USER admin WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE app TO admin;
python manage.py makemigrations 
python manage.py migrate
python manage.py loaddata dbinit.db
python manage.py runserver 