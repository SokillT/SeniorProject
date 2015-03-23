# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20150323_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Cid', models.IntegerField(serialize=False, primary_key=True)),
                ('CatType', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('Nid', models.AutoField(serialize=False, primary_key=True)),
                ('Topic', models.CharField(max_length=100)),
                ('Link', models.CharField(max_length=100)),
                ('Date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcate',
            fields=[
                ('Sid', models.IntegerField(serialize=False, primary_key=True)),
                ('SubType', models.CharField(max_length=50)),
                ('Cid', models.ForeignKey(to='news.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
