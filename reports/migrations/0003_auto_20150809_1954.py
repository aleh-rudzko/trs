# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20150809_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='tasks',
            field=models.ForeignKey(to='tasks.Task', related_name='tasks'),
        ),
    ]
