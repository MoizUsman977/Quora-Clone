# Generated by Django 4.2.2 on 2023-06-21 18:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_remove_user_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_pictures'),
        ),
    ]
