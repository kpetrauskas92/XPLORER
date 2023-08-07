# Generated by Django 3.2.20 on 2023-08-02 17:29

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to='auth.user', verbose_name='user')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.TextField(blank=True, max_length=200, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_image')),
            ],
        ),
    ]