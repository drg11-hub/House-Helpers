# Generated by Django 3.0.3 on 2020-05-13 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Queries', '0013_auto_20200513_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electrical',
            name='City',
        ),
        migrations.RemoveField(
            model_name='housekeeping',
            name='City',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='City',
        ),
        migrations.RemoveField(
            model_name='plumber',
            name='City',
        ),
        migrations.RemoveField(
            model_name='salon',
            name='City',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='City',
        ),
    ]
