# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(unique=True, max_length=14)),
                ('status', models.BooleanField()),
                ('pin', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('balance', models.BooleanField()),
                ('paymant', models.FloatField()),
                ('transaction_status', models.IntegerField()),
                ('card_number', models.ForeignKey(to='cash.Card')),
            ],
        ),
    ]
