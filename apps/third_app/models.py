from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    enroll_date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    gender = models.CharField(choices=[('male', "Male"), ('female', 'Female')],blank=False)



