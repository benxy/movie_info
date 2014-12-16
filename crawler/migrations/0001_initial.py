# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=1024)),
                ('last_search_date', models.DateTimeField(default=datetime.datetime.now, auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
