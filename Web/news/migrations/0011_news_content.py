# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20150323_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
