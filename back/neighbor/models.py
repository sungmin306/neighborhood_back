from django.db import models
from django.conf import settings
# Create your models here.

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimestampedModel):
    pass