# Generated by Django 3.2.19 on 2023-06-22 10:43

import My_plant_project.my_plant_app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_plant_app', '0003_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), My_plant_project.my_plant_app.models.validate_string_contains_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
