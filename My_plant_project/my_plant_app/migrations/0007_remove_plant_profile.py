# Generated by Django 3.2.19 on 2023-06-22 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_plant_app', '0006_plant_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='profile',
        ),
    ]
