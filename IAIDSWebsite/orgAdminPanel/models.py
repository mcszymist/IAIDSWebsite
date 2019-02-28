from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    personel = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()


