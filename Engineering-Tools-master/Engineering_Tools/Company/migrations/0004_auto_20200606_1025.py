# Generated by Django 3.0.1 on 2020-06-06 04:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0003_product_software_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_software',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_software',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]