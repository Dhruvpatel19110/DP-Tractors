# Generated by Django 4.0.1 on 2022-04-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0057_oldtractor_name_alter_oldtractor_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oldtractor',
            name='Back_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Engine1_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Engine_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Leftside_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Meter_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Rightside_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Tyare1_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Tyare2_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Tyare3_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Tyare4_Photo',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='Video',
            field=models.FileField(upload_to='videos_uploaded'),
        ),
        migrations.AlterField(
            model_name='oldtractor',
            name='upload',
            field=models.ImageField(upload_to='images'),
        ),
    ]
