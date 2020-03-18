from django.contrib import admin
from .models import goods,good_class
# Register your models here.

#把goods数据表注册到admin后台管理系统

@admin.register(goods)
class goodAdmin(admin.ModelAdmin):
    #栏目展示项
    list_display = ("name","classification","date")
    #排序码设定
    ordering = ["-id"]

@admin.register(good_class)
class goodclassadmin(admin.ModelAdmin):
    list_display = ("cname","id")
