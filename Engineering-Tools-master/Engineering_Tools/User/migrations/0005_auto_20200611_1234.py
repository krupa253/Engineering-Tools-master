# Generated by Django 3.0.1 on 2020-06-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20200611_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=6),
        ),
    ]
