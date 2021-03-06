# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_todo', '0004_auto_20160216_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='collaborators',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(help_text='Please enter task description', max_length=2000),
        ),
        migrations.AlterField(
            model_name='task',
            name='isComplete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(help_text='Please enter task title', max_length=2000),
        ),
    ]
