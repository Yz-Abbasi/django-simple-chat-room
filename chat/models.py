from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=600)


class Message(models.Model):
    msg = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=False)
    user = models.CharField(max_length=50)
    room = models.CharField(max_length=600)
