# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 15:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_todo', '0002_auto_20160215_0014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='fl_name',
        ),
    ]
