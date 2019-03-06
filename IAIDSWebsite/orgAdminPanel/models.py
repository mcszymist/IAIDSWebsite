from django.db import models
from createAccount.models import MyUser
from datetime import datetime  
# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(default='Please Fill')
    def __str__(self):
        return '%s' % (self.name)

class Event(models.Model):
    orgID = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 100)
    description = models.TextField(default='Please Fill')
    personelMax = models.PositiveIntegerField(default=1)
    personel = models.PositiveIntegerField(default=0)
    location = models.CharField(default="", max_length=100)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return '%s %s' % (self.name,self.id)


class EventVol(models.Model):
    eventID = models.ManyToManyField(Event)
    userID = models.ManyToManyField(MyUser)
    status = models.BooleanField(default=False)

class OrganizationUsers(models.Model):
    orgID = models.ManyToManyField(Organization)
    userID = models.ManyToManyField(MyUser)
    privledge = models.PositiveIntegerField(default=0)


	


