from django.db import models

# Create your models here.

class Permission(models.Model):
    title=models.CharField(verbose_name='权限标题',max_length=32)
    url=models.CharField(verbose_name='权限url',max_length=128)
    ismenu=models.BooleanField(verbose_name='是否是菜单',default=True)
    parentid=models.CharField(verbose_name='父菜单id',max_length=32)
    def __str__(self):
        return self.title

class Role(models.Model):
    title=models.CharField(verbose_name='角色名称',max_length=32)
    permission=models.ManyToManyField(to='Permission',verbose_name='角色对应权限',blank=True)
    def __str__(self):
        return self.title

class User(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    roles=models.ManyToManyField(to='Role',verbose_name='用户对应角色',blank=True)
    def __str__(self):
        return self.username