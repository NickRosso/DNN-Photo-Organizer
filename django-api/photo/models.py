from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Photo(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    path = models.ImageField(upload_to='uploads/')
    classification = models.TextField(blank=True)
