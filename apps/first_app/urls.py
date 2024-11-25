from django.contrib import admin
from django.urls import path, include
from .views import hello_world, about, contact

urlpatterns = [
    path('home', hello_world ),
    path('about', about),
    path('contact', contact),
]