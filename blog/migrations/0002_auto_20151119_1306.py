# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=models.TextField(verbose_name=b'Text of Article'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Publication date'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name=b"Insert tags for Article,i.e.'Python,Django etc.'"),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'Title of Article'),
        ),
    ]
