# Generated by Django 3.2.19 on 2023-06-22 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_plant_app', '0005_auto_20230622_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_plant_app.profile'),
            preserve_default=False,
        ),
    ]