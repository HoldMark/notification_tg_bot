# celery_app.py

from celery import Celery

app = Celery('tasks', broker='sqla+sqlite:///example.sqlite')
