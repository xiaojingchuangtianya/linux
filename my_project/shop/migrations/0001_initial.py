# Generated by Django 2.0 on 2020-02-29 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='good_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('picture_url', models.URLField()),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.good_class')),
            ],
        ),
        migrations.CreateModel(
            name='own',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Oname', models.CharField(max_length=20)),
                ('Ologin', models.BigIntegerField(unique=True)),
                ('Opassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.own'),
        ),
    ]
