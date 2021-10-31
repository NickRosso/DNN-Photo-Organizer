from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import classify_photo

class Photo(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    path = models.ImageField(upload_to='uploads/')
    classification = models.TextField(blank=True)


@receiver(post_save, sender=Photo, dispatch_uid="Photo")
def classify_photo(sender, instance, **kwargs):
    """ post_save method to trigger celery async task for classification
        input: photo object instance
        returns: None
    """
    classify_photo.apply_async(args=[instance])
    