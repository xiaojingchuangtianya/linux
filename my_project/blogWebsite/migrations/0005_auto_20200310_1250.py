# Generated by Django 2.0 on 2020-03-10 04:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogWebsite', '0004_auto_20200309_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='read_count',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='read_count',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]