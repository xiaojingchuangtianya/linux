from django.contrib import admin
from .models import Blog_type,Blog,Read_count

# Register your models here.
@admin.register(Blog_type)
class Blog_typeadmin(admin.ModelAdmin):
    list_display = ("type_name","id")

@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    list_display = ("title","blog_type","auth_foreign","create_time","read_count")

@admin.register(Read_count)
class Read_countadmin(admin.ModelAdmin):
    list_display = ("read_num","blog")