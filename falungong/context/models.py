from django.db import models

# Create your models here.
class Context(models.Model):
    title=models.CharField(max_length=30)
    fenlei=models.CharField(max_length=20)
    neirong=models.CharField(max_length=20000)
    status=models.BooleanField(default=True)
    class Meta:
        db_table='t_context'

class Pic(models.Model):
    img = models.ImageField(upload_to="static/img/up_pic")
