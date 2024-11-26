from django.contrib import admin
from django.urls import path, include
from .views import demo1,demo2,demo3

urlpatterns = [
    path('demo1/<int:id>/', demo1),
    path('demo2', demo2),
    path('demo3', demo3),
]