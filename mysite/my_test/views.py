from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Tech with Nushan</h1><br/><a href='http://127.0.0.1:5050/starts/'>Link</a>")

def v1(response):
    return HttpResponse("<h1>view 1!</h1>")