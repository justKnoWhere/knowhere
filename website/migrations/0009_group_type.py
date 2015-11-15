# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20151112_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='type',
            field=models.CharField(max_length=7, choices=[('public', 'Public'), ('private', 'Private'), ('secret', 'Secret')], default='public'),
        ),
    ]
