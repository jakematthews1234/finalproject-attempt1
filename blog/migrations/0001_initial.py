# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-23 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('summary', models.CharField(max_length=240)),
                ('blog_body', models.TextField()),
                ('date_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
