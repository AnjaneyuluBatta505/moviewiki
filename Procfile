web:python manage.py runserver
web: gunicorn moviewiki.wsgi --log-file -
heroku ps:scale web=1
