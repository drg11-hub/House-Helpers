# Generated by Django 3.0.3 on 2020-04-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Houses', '0009_customer_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Contact',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Email',
            field=models.EmailField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='First_Name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Last_Name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
