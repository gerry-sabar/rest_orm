Requirements:
1. python3
2. postgresql

Installation:

1. clone the project
2. create virtual environment inside root project:
   python3 -m venv venv
3. pip install -r requirements.txt
4. create .env in /rest_orm according to your postgre setting with setting as follow:
    DEBUG = True
    SECRET_KEY = "pt@uy%2tf0akqi0&a)b$rcu6p2#&o-^c-skl*0-i$2^4nx8=!+"
    DB_NAME = "YOUR_DATABASE_NAME"
    DB_USER = "YOUR_DATABASE_USERNAME"
    DB_PASSWORD = "YOUR_DATABASE_PASSWORD"
    DB_HOST = "YOUR_DATABASE_HOST"
5. python manage.py migrate
6. python manage.py loaddata fixtures.json
7. python manage.py runserver
8. your development server is ready 