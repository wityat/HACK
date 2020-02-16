from django.db import models

# Create your models here.


class SiteUser(models.Model):
    session_key = models.CharField("session_key", max_length=200)
    image = models.ImageField("image", upload_to="media/", null=True, blank=True)
