from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    volMax = models.IntegerField()
    volCurrent = models.IntegerField()
    location = models.CharField(max_length=100)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    uid = models.UUIDField(primary_key=True)
    