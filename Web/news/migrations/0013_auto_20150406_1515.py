# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20150331_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='Date',
            new_name='DatePublish',
        ),
    ]
