from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def movies(request):
    template = loader.get_template('MTW.html')
    return HttpResponse(template.render())