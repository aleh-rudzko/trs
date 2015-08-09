# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='admin',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 9, 15, 56, 0, 392382, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(related_name='available_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 9, 15, 56, 6, 583736, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 9, 15, 56, 10, 751974, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 9, 15, 56, 22, 183628, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
