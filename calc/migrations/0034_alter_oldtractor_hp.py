# Generated by Django 4.0.1 on 2022-03-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0033_oldtractor_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oldtractor',
            name='HP',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
    ]
