from __future__ import absolute_import, unicode_literals
from photo_organizer.celery import app
from celery import shared_task
import requests

@shared_task
def test(self):
    print("test")