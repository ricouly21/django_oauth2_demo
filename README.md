# Django OAuth2 Demo

This is a simple backend application with basic Django models and OAuth2.0 integration using ```django-oauth-toolkit```. This project uses PostgreSQL for the database.

## Installation
1. Create a PostgreSQL database.
2. Rename ```django_demo/.env.copy``` into ```django_demo/.env``` and replace these values.
```
# PostgreSQL Database
DB_NAME = <Name of Database>
DB_USER = <Name of Database Owner>
DB_HOST = <Database host address (default: 127.0.0.1)>
DB_PORT= <Database port (default: 5432)>
```
3. Enter these commands on your terminal to run the app:
```
pip install -r requirements.txt
python manage.py makemigrations accounts
python manage.py migrate
python manage.py runserver 0:8080
```

## Contributors
* ULY Rico

