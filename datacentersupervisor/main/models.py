from django.db import models
from datetime import datetime

# Create your models here.

class Collection(models.Model):
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    gas = models.FloatField(null=True, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)