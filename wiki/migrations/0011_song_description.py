# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-06 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0010_person_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]