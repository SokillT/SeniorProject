# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_news_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Content',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
