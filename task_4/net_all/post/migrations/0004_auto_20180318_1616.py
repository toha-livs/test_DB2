# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-18 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20180318_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userall',
            old_name='emil_confirm',
            new_name='email_confirm',
        ),
    ]
