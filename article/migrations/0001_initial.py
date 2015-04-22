# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_title', models.CharField(max_length=200)),
                ('article_text', models.TextField()),
                ('article_pub_date', models.DateTimeField()),
                ('article_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'article',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_text', models.TextField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9')),
                ('comments_acticle', models.ForeignKey(to='article.Article')),
            ],
            options={
                'db_table': 'comments',
            },
            bases=(models.Model,),
        ),
    ]
