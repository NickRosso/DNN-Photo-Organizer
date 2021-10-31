from django.db import models
from tasks import classify_photo

class Photo(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    path = models.ImageField(upload_to='media/')
    classification = models.TextField()

""" post_save method to classify uploaded photo
    input: photo object
    returns: None
"""
@receiver(post_save, sender=Photo, dispatch_uid="Photo")
def classify_photo(sender, instance, **kwargs):
    classify_photo.apply_async(args=[instance])
    