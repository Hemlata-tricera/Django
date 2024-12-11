from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('stud', views.student_detail, name='all_students'),
    path('add', views.add_student, ),
    path('delete', views.add_student, ),
    path('edit', views.add_student, ),


]
