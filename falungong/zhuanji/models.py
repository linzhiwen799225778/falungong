from django.db import models

# Create your models here.
class zhuanjis(models.Model):
    title = models.CharField(max_length=15)
    score = models.CharField(max_length=15)
    author = models.CharField(max_length=15)
    boyin = models.CharField(max_length=15)
    zhangjieshu = models.CharField(max_length=15)
    jianjie = models.CharField(max_length=150)
    statue = models.BooleanField(default=True)
    pic = models.CharField(max_length=15)


class zhangjie(models.Model):
    zhangjie_name=models.CharField(max_length=20)
    zhangjie_size=models.CharField(max_length=20)
    url=models.ImageField(upload_to='static/audio/')
    zj_id = models.ForeignKey(to='zhuanjis',on_delete=models.CASCADE)

# class ZhuanjiZhangjie(models.Model):
#     zhangjie_name = models.CharField(max_length=20)
#     zhangjie_size = models.CharField(max_length=20)
#     zhangjie_time = models.CharField(max_length=20)
#     url = models.CharField(max_length=255)
#     zhuanji = models.ForeignKey('ZhuanjiZhunji', models.CASCADE)
#
#
#
# class ZhuanjiZhunji(models.Model):
#     title = models.CharField(max_length=15)
#     score = models.CharField(max_length=15)
#     author = models.CharField(max_length=15)
#     boyin = models.CharField(max_length=15)
#     zhangjie = models.CharField(max_length=15)
#     jianjie = models.CharField(max_length=150)
#     statue = models.IntegerField()
#     pic = models.CharField(max_length=255)



