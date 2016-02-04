# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cash', '0003_auto_20160111_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='transaction_status',
        ),
    ]
