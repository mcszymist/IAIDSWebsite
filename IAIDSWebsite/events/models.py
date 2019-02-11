from django.db import models

# Create your models here.
class Event(models.Model):
    UniqueCode = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=300)
    Organization = models.CharField(max_length=100)
    typeOfVol = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    startDate = models.DateTimeField('date published')
    endDate = models.DateTimeField('date published')
    