from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def userDisplay(request):
    return HttpResponse('<h1>This is User Response</h2>')