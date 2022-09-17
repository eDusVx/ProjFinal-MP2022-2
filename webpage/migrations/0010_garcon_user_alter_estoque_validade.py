# Generated by Django 4.1 on 2022-09-15 00:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webpage', '0009_alter_estoque_validade_alter_pedido_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='garcon',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='validade',
            field=models.DateField(default=datetime.datetime(2022, 9, 14, 21, 52, 25, 172855)),
        ),
    ]