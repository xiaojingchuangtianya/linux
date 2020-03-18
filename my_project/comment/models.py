from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)#定义好外键关联类型
    object_id = models.PositiveIntegerField()#关联类型的主键
    content_object =GenericForeignKey("content_type","object_id")#根据以上两个字段获取到唯一的数据

    comment = models.TextField()
    edit_time =models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    class Meta:
        ordering =["-edit_time"]
