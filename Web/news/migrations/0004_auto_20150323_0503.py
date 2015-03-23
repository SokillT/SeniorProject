# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150216_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcate',
            fields=[
                ('Sid', models.IntegerField(serialize=False, primary_key=True)),
                ('SubType', models.CharField(max_length=50)),
                ('Cid', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Type',
            new_name='CatType',
        ),
        migrations.RemoveField(
            model_name='news',
            name='Cid',
        ),
        migrations.AddField(
            model_name='news',
            name='Date',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 5, 3, 44, 341071, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
