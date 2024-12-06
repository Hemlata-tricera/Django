# from django.contrib import admin
# from django.db import models
#
# # Register your models here.
# class Student(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     date_of_birth = models.DateField()
#
#
#     enrollment_date = models.DateField(auto_now_add=True)
#
#     stud_pass_img = models.ImageField(upload_to='students/profiles/', null=True, blank=True)
#
#     # File field for an uploaded document (e.g., transcript, assignments, etc.)
#     enroll_doc = models.FileField(upload_to='students/enrollments/', null=True, blank=True)
