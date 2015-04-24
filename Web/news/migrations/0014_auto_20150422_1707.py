# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20150406_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news2sub',
            name='Nid',
        ),
        migrations.RemoveField(
            model_name='news2sub',
            name='Sid',
        ),
        migrations.DeleteModel(
            name='News2Sub',
        ),
        migrations.AlterField(
            model_name='news',
            name='DatePublish',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
