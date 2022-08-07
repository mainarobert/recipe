from django.urls import path
from . import views

urlpatterns = [
    path('', views.userDisplay, name='userDisplay'),
]