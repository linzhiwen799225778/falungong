from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    sex=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    salt=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    headpic=models.CharField(max_length=20)
    status=models.CharField(max_length=20)