# Generated by Django 4.0.1 on 2022-04-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0055_remove_oldtractor_hp1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldtractor',
            name='name',
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='upload',
            field=models.ImageField(upload_to='images'),
        ),
    ]