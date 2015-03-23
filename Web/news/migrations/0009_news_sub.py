# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_category_news_subcate'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_sub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nid', models.ForeignKey(to='news.News')),
                ('Sid', models.ForeignKey(to='news.Subcate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
