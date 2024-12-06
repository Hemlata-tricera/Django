from django.contrib import admin
from django.urls import path, include
from .views import hello_world, about, contact, MyView

urlpatterns = [

    path('home/<int:id>', hello_world ),
    path('about', about),
    path('contact', contact),
    path('cl', MyView.as_view())
]