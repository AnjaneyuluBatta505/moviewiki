web:python manage.py runserver
web:python manage.py makemigrations
web:python manage.py migrate
web: gunicorn moviewiki.wsgi --log-file -
heroku ps:scale web=1
