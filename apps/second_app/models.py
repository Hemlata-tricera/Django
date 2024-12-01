from django.db import models

# Create your models here.
class Transactions(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    transaction_date = models.DateField()


class Students(models.Model):
    stu_id = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(Students,on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)