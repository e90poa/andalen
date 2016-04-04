# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'name')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'name')),
            ],
        ),
        migrations.CreateModel(
            name='TagTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.ForeignKey(verbose_name=b'tag', to='tasks.Tag')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date modified'),
        ),
        migrations.AddField(
            model_name='tagtask',
            name='task',
            field=models.ForeignKey(verbose_name=b'task', to='tasks.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='folder',
            field=models.ForeignKey(verbose_name=b'folder', to='tasks.Folder', null=True),
        ),
    ]
