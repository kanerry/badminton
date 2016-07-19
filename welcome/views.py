import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
import datetime
import requests

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
    
def index(request):
    r = requests.get("http://www.51hlife.com/b2b/welcome.htm")
    return r.content

def health(request):
    return HttpResponse(PageView.objects.count())
