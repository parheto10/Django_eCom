# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-17 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paniers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='panier',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
