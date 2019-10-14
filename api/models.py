from django.db import models
from datetime import timedelta


class Package(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price =models.PositiveIntegerField()
    destination = models.CharField(max_length=10)
    duration = models.DurationField(default=timedelta(days=5))
    
