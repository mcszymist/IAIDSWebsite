from django.db import models
from createAccount.models import MyUser

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    personelMax = models.PositiveIntegerField()
    personel = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()

class Organization(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()
	
class EventVol(models.Model):
	eventID = models.ManyToManyField(Event)
	userID = models.ManyToManyField(MyUser)
	status = models.BooleanField()

class OrganizationUsers(models.Model):
	orgID = models.ManyToManyField(Organization)
	userID = models.ManyToManyField(MyUser)
	privledge = models.PositiveIntegerField()
	


