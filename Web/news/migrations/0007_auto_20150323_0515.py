# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_category_news_subcate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.RemoveField(
            model_name='subcate',
            name='Cid',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Subcate',
        ),
    ]
