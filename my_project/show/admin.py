from django.contrib import admin
from .models import day_sight
# Register your models here.
@admin.register(day_sight)
class sightadmin(admin.ModelAdmin):
    list_display = ("day_count","read_date")
