# Generated by Django 4.1 on 2022-09-06 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediente',
            name='colesterol',
            field=models.FloatField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='validade',
            field=models.DateField(default=datetime.datetime(2022, 9, 6, 8, 34, 25, 200627)),
        ),
    ]
