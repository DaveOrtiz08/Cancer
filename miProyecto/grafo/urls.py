from django.contrib import admin
from django.urls import path
from .views import grafos

app_name = "grafo"

urlpatterns = [
    path('',grafos, name="grafo")
]
