web: python manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT djangoProject/settings.py
web: gunicorn djangoProject.wsgi --log-file -

