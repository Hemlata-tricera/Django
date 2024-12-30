from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('stud', views.student_detail, name='all_students'),  # View all students
    path('add', views.add_student, name='add_student'),  # Add new student
    path('delete', views.add_student, name='delete_student'),  # Delete student
    path('update/<int:rollno>/', views.update, name='update'),  # Update student details form
    path('updaterecord/<int:rollno>/', views.updaterecord, name='updaterecord'),  # Process student update
]
