from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q

from orgAdminPanel.models import Event

from allauth.account.views import LoginView
from allauth.account.forms import LoginForm

from .forms import MyCustomLoginForm

from datetime import datetime, date, timedelta

# Create your views here.


def index(request):
    startdateBegin = datetime.today()
    startdateEnd = startdateBegin + timedelta(days=7)
    starttimeBegin = datetime.time(datetime.now())

    testArray = [startdateBegin, startdateEnd]
    upcomingEvents = Event.objects.all().order_by(
        'startdate', 'starttime', 'name').filter(startdate__range=[startdateBegin, startdateEnd],
                                                 starttime__gte=starttimeBegin)
    return render(request, 'home.html',
                  {'testArray': testArray,
                   'upcomingEvents': upcomingEvents})
