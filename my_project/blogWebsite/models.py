from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
# Create your models here

class Blog_type(models.Model):
    type_name=models.CharField(max_length=10)
    def __str__(self):
        return self.type_name




class Blog(models.Model):
    title=models.CharField(max_length=30)#标题
    blog_type=models.ForeignKey(Blog_type,on_delete=models.DO_NOTHING)#博客类型，以外键链接Blog_type
    text=RichTextUploadingField()#文章主题，富文本
    auth_foreign=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)#用户
    create_time=models.DateTimeField(auto_now_add=True)#创建时间

    def __str__(self):#展示字段
        return self.title
    class Meta:#设置此处为了让paginator分页时排序
        ordering=["-create_time"]

#阅读计数字段
class Read_count(models.Model):
    read_num=models.IntegerField(default=0)
    blog =models.OneToOneField(Blog,on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.read_num)


