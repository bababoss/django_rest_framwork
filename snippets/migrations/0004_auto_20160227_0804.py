# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20160227_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='created',
            field=models.DateField(null=True),
        ),
    ]
