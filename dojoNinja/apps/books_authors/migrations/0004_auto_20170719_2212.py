# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors', '0003_auto_20170719_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]