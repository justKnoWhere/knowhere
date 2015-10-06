# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('users', models.ManyToManyField(to='website.User')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=64)),
                ('zipcode', models.CharField(max_length=64)),
                ('date', models.DateField(max_length=64)),
                ('time', models.DateTimeField(max_length=64)),
                ('groups', models.ManyToManyField(to='website.Group')),
                ('user', models.ForeignKey(to='website.User')),
            ],
        ),
    ]
