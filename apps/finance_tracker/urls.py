from django.contrib import admin
from django.urls import path, include
from .views import func_base

urlpatterns = [
    path('fun', func_base)



]
