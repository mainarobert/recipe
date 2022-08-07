from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displayApp(request):
    return HttpResponse('<h1>This is App response</h1>')
