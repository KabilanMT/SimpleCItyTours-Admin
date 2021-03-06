# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='polygon',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='polygon',
            name='fillOpacity',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='polygon',
            name='strokeOpacity',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
