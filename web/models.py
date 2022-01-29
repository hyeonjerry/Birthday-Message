from django.db import models
from django.utils import timezone


class Message(models.Model):
    name = models.CharField(max_length=8)
    message = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
