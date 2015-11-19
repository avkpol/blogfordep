# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.CharField(max_length=25)),
                ('requested_url', models.CharField(max_length=255)),
                ('request_type', models.CharField(max_length=10)),
                ('request_ip', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('skype', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
