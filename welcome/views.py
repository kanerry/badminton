import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
import datetime
import urllib2

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
    
def index(request):
    url = 'http://www.baidu.com/'
    response = urllib2.urlopen(url) ##urlopen接受传入参数是string或者是request
    response_text = response.read()
    return response_text

def health(request):
    return HttpResponse(PageView.objects.count())
