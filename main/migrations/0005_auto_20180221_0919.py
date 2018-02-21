# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180216_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date_and_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
