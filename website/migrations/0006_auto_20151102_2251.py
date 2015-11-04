# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20151015_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='latitude',
            field=models.DecimalField(default=0.0, decimal_places=6, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='longitude',
            field=models.DecimalField(default=0.0, decimal_places=6, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notificationzone',
            name='groups',
            field=models.ManyToManyField(to='website.Group', blank=True),
        ),
    ]
