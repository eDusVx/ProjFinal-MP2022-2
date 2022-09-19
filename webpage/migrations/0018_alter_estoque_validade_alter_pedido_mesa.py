# Generated by Django 4.1 on 2022-09-19 01:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("webpage", "0017_alter_estoque_validade_alter_pedido_mesa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="estoque",
            name="validade",
            field=models.DateField(
                default=datetime.datetime(2022, 9, 18, 22, 30, 49, 880165)
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="mesa",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="webpage.mesa",
            ),
        ),
    ]
