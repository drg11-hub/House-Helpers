# Generated by Django 3.0.3 on 2020-05-13 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Queries', '0012_auto_20200513_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housekeeping',
            name='City',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='massage',
            name='City',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='plumber',
            name='City',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='salon',
            name='City',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='City',
            field=models.CharField(max_length=10),
        ),
    ]
