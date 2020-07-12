# Django OAuth2 Demo

This is a simple backend application with basic Django models and OAuth2 integration using ```django-oauth-toolkit```. This application uses PostgreSQL for the database.

## Installation
1. Create a PostgreSQL database.
2. Edit ```Settings.py``` and replace these values with your own database details.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': <db_name>,
        'USER': <db_user>,
        'HOST': <db_host>,
        'PORT': <db_port>
    }
}
```
3. Run these commands to run the app:
```
python manage.py migrate
python manage.py makemigrations accounts
python manage.py runserver
```

## Contributors
* ULY Rico

