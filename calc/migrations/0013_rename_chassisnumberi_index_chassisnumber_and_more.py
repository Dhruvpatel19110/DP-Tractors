# Generated by Django 4.0.1 on 2022-03-10 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0012_rename_model_index_kmdriveni_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='ChassisNumberi',
            new_name='ChassisNumber',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='KMDriveni',
            new_name='KMDriven',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='RCi',
            new_name='RC',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='Regnoi',
            new_name='Regno',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='desti',
            new_name='dest',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='modeli',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='namei',
            new_name='name',
        ),
    ]
