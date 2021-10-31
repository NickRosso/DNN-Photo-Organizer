from django.db import models
from tasks import test
# Create your models here.

class Photo(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=1024, default="")
    path = models.ImageField(upload_to='media/')
    tags = models.TextField()


# method for updating
@receiver(post_save, sender=Photo, dispatch_uid="Photo")
def classify_image(sender, instance, **kwargs):
    test.apply_async(args=[])
    