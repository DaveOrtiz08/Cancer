from django.contrib import admin
from django.urls import path
from .views import home, nohome

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    
]

