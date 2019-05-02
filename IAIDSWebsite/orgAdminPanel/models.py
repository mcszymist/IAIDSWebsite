from django.db import models
from createAccount.models import MyUser
from datetime import datetime
# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(default='What is your organization about?')
    def __str__(self):
        return '%s' % (self.name)

class Event(models.Model):
    orgID = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 100)
    description = models.TextField(default='What is this event about?')
    location = models.CharField(default="", max_length=100)
    startdate = models.DateField(default=datetime.today)
    enddate = models.DateField(default=datetime.today)
    starttime = models.TimeField(default=datetime.time(datetime.now()))
    endtime = models.TimeField(default=datetime.time(datetime.now()))
    def __str__(self):
        return '%s %s' % (self.name,self.id)

    def fullCallendarStartFormat(self):
        front = self.startdate.strftime('%Y-%m-%d')
        end = self.starttime.strftime('T%H:%M:%S')
        return front + end

    def fullCallendarEndFormat(self):
        front = self.enddate.strftime('%Y-%m-%d')
        end = self.endtime.strftime('T%H:%M:%S')
        return front + end

class EventVol(models.Model):
    eventID = models.ManyToManyField(Event)
    userID = models.ManyToManyField(MyUser)
    status = models.BooleanField(default=False)

class OrganizationUsers(models.Model):
    orgID = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    userID = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    privledge = models.PositiveIntegerField(default=0)

class Job(models.Model):
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    userID = models.ManyToManyField(MyUser)
    name = models.CharField(max_length = 100)
    personelMax = models.PositiveIntegerField(default=1)
    personel = models.PositiveIntegerField(default=0)
    startdate = models.DateField(default=datetime.today)
    enddate = models.DateField(default=datetime.today)
    starttime = models.TimeField(default=datetime.time(datetime.now()))
    endtime = models.TimeField(default=datetime.time(datetime.now()))
    description = models.TextField(default='What is this job about?')
    def amountPersonalNeeded(self):
        return self.personelMax - self.personel
    

