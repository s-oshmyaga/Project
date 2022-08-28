# Generated by Django 4.1 on 2022-08-23 13:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JunJob', '0004_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(max_length=10000, upload_to='company_images'),
        ),
    ]
