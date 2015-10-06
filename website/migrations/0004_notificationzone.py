# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20151006_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationZone',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('address', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=64)),
                ('zipcode', models.CharField(max_length=64)),
                ('radius', models.DecimalField(max_digits=9, decimal_places=2)),
                ('groups', models.ManyToManyField(to='website.Group')),
                ('user', models.ForeignKey(to='website.User')),
            ],
        ),
    ]
