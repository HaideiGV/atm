# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0002_auto_20160106_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='balance',
            new_name='show_balance',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='paymant',
            new_name='sum_withdrawal',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='date',
            new_name='transaction_time',
        ),
        migrations.AddField(
            model_name='card',
            name='amount',
            field=models.IntegerField(default=1, verbose_name=b'Cash amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transactions',
            name='input_pin',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transactions',
            name='try_pin',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transactions',
            name='card_number',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_status',
            field=models.BooleanField(),
        ),
    ]
