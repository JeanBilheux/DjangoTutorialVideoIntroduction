# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 01:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_auto_20160909_0104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
