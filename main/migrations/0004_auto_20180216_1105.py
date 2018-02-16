# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180214_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='palyer2_score',
            new_name='player2_score',
        ),
    ]
