# Generated by Django 4.0.1 on 2022-04-21 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0053_oldtractor_min_prize'),
    ]

    operations = [
        migrations.AddField(
            model_name='oldtractor',
            name='HP1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
