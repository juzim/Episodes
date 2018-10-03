# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow', '0004_auto_20160727_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='date_watched',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]