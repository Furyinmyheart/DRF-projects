from django.shortcuts import render
from .models import campaign
from .models import channel

def campaing_view():
    return render(request=campaign, index.html)

def channel_view():
    return render(request=channel, index.html)