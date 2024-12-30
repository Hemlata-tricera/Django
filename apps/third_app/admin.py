from django.contrib import admin
from django.db import models
from .models import Student




class StudentAdmin(admin.ModelAdmin):
    list_display = ('rollno','fname','lname','enroll_date')

admin.site.register(Student, StudentAdmin)