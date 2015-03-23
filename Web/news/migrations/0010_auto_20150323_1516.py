# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_news_sub'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News_sub',
            new_name='News2Sub',
        ),
    ]
