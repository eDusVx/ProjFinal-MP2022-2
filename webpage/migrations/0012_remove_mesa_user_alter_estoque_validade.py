# Generated by Django 4.1 on 2022-09-15 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0011_mesa_user_alter_estoque_validade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesa',
            name='user',
        ),
        migrations.AlterField(
            model_name='estoque',
            name='validade',
            field=models.DateField(default=datetime.datetime(2022, 9, 15, 16, 28, 34, 573849)),
        ),
    ]
