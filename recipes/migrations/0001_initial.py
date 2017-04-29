# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 21:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500, validators=[django.core.validators.URLValidator])),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
            ],
        ),
    ]
