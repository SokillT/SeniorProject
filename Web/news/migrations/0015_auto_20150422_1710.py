# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20150422_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cid', models.ForeignKey(to='news.Category')),
                ('Nid', models.ForeignKey(to='news.News')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='news',
            name='Link',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='Topic',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
