from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name='update'),
    path('new', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
]