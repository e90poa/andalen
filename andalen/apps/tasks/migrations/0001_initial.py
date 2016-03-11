# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'name')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'name')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=b'name')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
