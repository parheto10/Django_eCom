# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=39.0, max_digits=10),
        ),
    ]
