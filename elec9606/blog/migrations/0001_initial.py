# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=100)),
                ('user_gender', models.CharField(max_length=6)),
                ('user_email', models.CharField(max_length=50)),
                ('user_regdate', models.DateTimeField(verbose_name='Date registed.')),
            ],
        ),
    ]