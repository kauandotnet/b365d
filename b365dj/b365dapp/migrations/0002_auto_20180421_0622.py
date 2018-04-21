# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b365dapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currenteventstate',
            options={'ordering': ['created_at'], 'verbose_name': 'Current Event State', 'verbose_name_plural': 'Current Event States'},
        ),
        migrations.RenameField(
            model_name='currenteventstate',
            old_name='event_start',
            new_name='period_start',
        ),
        migrations.RenameField(
            model_name='eventstate',
            old_name='event_start',
            new_name='period_start',
        ),
    ]