# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
