from django.db import models
from datetime import datetime

# Create your models here.

class Collection(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    gas = models.FloatField()
    date = models.DateTimeField(default=datetime.now, blank=True)