# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-24 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puns', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pun',
            new_name='PunWord',
        ),
    ]
