# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20150422_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Source',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
