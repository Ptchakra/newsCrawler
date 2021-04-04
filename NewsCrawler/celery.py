import os
from celery import Celery
import time
# from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsCrawler.settings')

app = Celery('NewsCrawler')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



@app.task(name="crawler_handler")
def crawler_handler():
    while True:
        print("handler print")
        time.sleep(5)
        print("out")