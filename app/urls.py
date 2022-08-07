from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayApp, name='displayApp'),
]