# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180214_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='result',
        ),
        migrations.AddField(
            model_name='match',
            name='palyer2_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='player1_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='field',
            field=models.ForeignKey(related_name='field', to='main.Field'),
        ),
    ]
