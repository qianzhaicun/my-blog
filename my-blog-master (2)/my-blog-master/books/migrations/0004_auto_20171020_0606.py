# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_opinionpoll_response'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['-name']},
        ),
        migrations.AddField(
            model_name='author',
            name='salutation',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
