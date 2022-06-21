from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# from django_celery_beat.models import PeriodicTask

app = Celery('tasks', broker='pyamqp://http://127.0.0.1:8000/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Verilist.settings')

app = Celery('Verilist')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-everyday-at-7': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=14, minute=28),
        #'args': ()
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')