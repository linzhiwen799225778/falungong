from django.db import models

# Create your models here.
class lunbo_picture(models.Model):
    desc=models.CharField(max_length=500)
    date=models.CharField(max_length=500)
    status=models.BooleanField(default=False)
    pic=models.ImageField(upload_to='static/img')



