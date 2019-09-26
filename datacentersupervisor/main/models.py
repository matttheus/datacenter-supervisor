from django.db import models
from datetime import datetime

# Create your models here.

class Temperature(models.Model):
    temperature = models.FloatField()
    date = models.DateTimeField(default=datetime.now, blank=True)


class Humidity(models.Model):
    humidity = models.FloatField()
    date = models.DateTimeField(default=datetime.now, blank=True)


class Gas(models.Model):
    gas = models.FloatField()
    date = models.DateTimeField(default=datetime.now, blank=True)