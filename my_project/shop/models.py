from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class good_class(models.Model):
     cname = models.CharField(max_length=10)#类别名字
     def __str__(self):
         return self.cname



class goods(models.Model):
    name=models.CharField(max_length=20)#商品名字
    classification = models.ForeignKey(good_class,on_delete=models.DO_NOTHING)#商品类别
    date=models.DateTimeField(auto_now_add=True)#时间
    price=models.FloatField()#价格
    description= models.TextField()#描述
    picture_url = models.URLField()#图片链接
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

