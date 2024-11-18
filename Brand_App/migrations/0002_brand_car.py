# Generated by Django 5.1.2 on 2024-11-18 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand_App', '0001_initial'),
        ('CurHub_App', '0002_remove_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='car',
            field=models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='CurHub_App.car'),
            preserve_default=1,
        ),
    ]