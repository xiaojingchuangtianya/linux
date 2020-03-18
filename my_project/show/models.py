from django.db import models
from django.utils import timezone

# Create your models here.
class day_sight(models.Model):
    day_count=models.IntegerField()
    read_date = models.DateField(timezone.now())

    class Meta:
        ordering=["-read_date"]
