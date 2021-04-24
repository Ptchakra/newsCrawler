from __future__ import absolute_import
import os
from celery import Celery
from datetime import datetime, timedelta
import time
from . import DoCrawler
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsCrawler.settings')
app = Celery('NewsCrawler')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    "crawler": {
        'task': 'test',
        'schedule': 300,
        'args': ('h'),
    }
}

@app.task(name = 'test')
def test(arg):
    print("hhhhhhhhhhh")
    DoCrawler.crawler_handler()
app.autodiscover_tasks()
# app.on_after_finalize()