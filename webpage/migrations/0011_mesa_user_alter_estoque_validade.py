# Generated by Django 4.1 on 2022-09-15 19:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webpage', '0010_garcon_user_alter_estoque_validade'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='validade',
            field=models.DateField(default=datetime.datetime(2022, 9, 15, 16, 28, 10, 113350)),
        ),
    ]
