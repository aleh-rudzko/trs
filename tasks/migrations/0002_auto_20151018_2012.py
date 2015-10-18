# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskMembership',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskmembership',
            name='task',
            field=models.ForeignKey(to='tasks.Task', verbose_name='task'),
        ),
        migrations.AddField(
            model_name='taskmembership',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
