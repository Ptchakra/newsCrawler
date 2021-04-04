"""
WSGI config for NewsCrawler project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

from asyncio.tasks import sleep
import os

import celery

from re import A

from django.core.wsgi import get_wsgi_application

from . import DoCrawler,celery

from multiprocessing import Pool

# def process_tasks():
    # os.system('python manage.py process_tasks')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsCrawler.settings')
application = get_wsgi_application()

# os.system("python manage.py process_tasks")
# pool = Pool(processes=1)
print("hello worlds")
celery.crawler_handler.apply_async()
print("have handle")