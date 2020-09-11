# Django OAuth2 Demo

This is a simple backend application with basic Django models and OAuth2 integration using ```django-oauth-toolkit```. This project uses PostgreSQL for the database.

## Installation
1. Create a PostgreSQL database.
2. Rename ```django_demo/.env.copy``` into ```django_demo/.env``` and replace these values.
```
# PostgreSQL Database
DB_NAME=<db_name>
DB_USER=<db_user>
DB_HOST=<db_host>
DB_PORT=<db_port>
```
3. Run these commands to run the app:
```
pip install -r requirements.txt
python manage.py makemigrations accounts
python manage.py migrate
python manage.py runserver 0:8080
```

## Contributors
* ULY Rico

