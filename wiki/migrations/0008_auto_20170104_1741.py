# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-04 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0007_auto_20161119_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]