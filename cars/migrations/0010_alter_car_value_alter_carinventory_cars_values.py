# Generated by Django 5.1 on 2024-09-06 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_car_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carinventory',
            name='cars_values',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
