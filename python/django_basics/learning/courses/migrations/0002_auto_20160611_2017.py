# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 03:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
