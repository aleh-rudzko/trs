# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150809_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='admin',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='projects'),
        ),
    ]
