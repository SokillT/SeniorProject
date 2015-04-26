# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                ('Topic', models.CharField(max_length=255)),
                ('Content', models.TextField(null=True, blank=True)),
                ('Link', models.CharField(max_length=255)),
                ('Source', models.CharField(max_length=50, null=True)),
                ('DatePublish', models.DateField(null=True)),
                ('DateStart', models.DateField(null=True)),
                ('Cid', models.ForeignKey(to='news.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News2Sub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nid', models.ForeignKey(to='news.News')),
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
        migrations.AddField(
            model_name='news2sub',
            name='Sid',
            field=models.ForeignKey(to='news.Subcate'),
            preserve_default=True,
        ),
    ]
