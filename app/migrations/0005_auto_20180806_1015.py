# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-06 17:15
from __future__ import unicode_literals

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180730_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='audioFile',
            field=models.FileField(null=True, upload_to=app.models.audioFileLocation),
        ),
    ]
