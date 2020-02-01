Requirements:
1. python3
2. postgresql

Installation:

1. clone the project
2. create virtual environment inside root project:
   python3 -m venv venv
3. pip install -r requirements.txt
4. adjust database setting in /rest_orm/.env according to your postgre setting
5. python manage.py migrate
6. python manage.py loaddata fixtures.json
7. python manage.py runserver
8. your development server is ready 