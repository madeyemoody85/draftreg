# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20170611_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftpod',
            name='draft_date',
            field=models.DateField(),
        ),
    ]