# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_group_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.TimeField(),
        ),
    ]
