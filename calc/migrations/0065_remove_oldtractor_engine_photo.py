# Generated by Django 4.0.1 on 2022-04-29 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0064_alter_oldtractor_back_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldtractor',
            name='Engine_Photo',
        ),
    ]