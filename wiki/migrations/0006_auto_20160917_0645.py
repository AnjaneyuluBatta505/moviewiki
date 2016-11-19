# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-17 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_movie_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='writers',
        ),
        migrations.AddField(
            model_name='song',
            name='writers',
            field=models.ManyToManyField(blank=True, null=True, related_name='get_songs', to='wiki.Person'),
        ),
    ]