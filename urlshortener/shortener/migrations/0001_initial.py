# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-11 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_url', models.CharField(max_length=220)),
                ('new_url', models.CharField(max_length=30)),
            ],
        ),
    ]
