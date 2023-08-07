# Generated by Django 3.2.20 on 2023-08-02 17:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='profile_image'),
        ),
    ]