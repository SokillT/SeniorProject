# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('Nid', models.AutoField(serialize=False, primary_key=True)),
                ('Topic', models.CharField(max_length=100)),
                ('Link', models.CharField(max_length=100)),
                ('Category', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
