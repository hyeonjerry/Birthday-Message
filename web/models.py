from django.db import models
from django.utils import timezone


class Message(models.Model):
    name = models.CharField(max_length=32)
    message = models.TextField()
    ip_address = models.CharField(max_length=16)
    create_date = models.DateTimeField(default=timezone.now)
