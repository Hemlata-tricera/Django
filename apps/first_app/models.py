from django.db import models

# Create your models here.
class Mymodel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
