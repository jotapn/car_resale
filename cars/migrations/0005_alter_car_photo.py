# Generated by Django 5.1 on 2024-08-28 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='cars'),
        ),
    ]
