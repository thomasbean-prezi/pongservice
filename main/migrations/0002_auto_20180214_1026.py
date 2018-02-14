# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='player1',
        ),
        migrations.AddField(
            model_name='match',
            name='player1',
            field=models.ManyToManyField(related_name='player1', to='main.Player'),
        ),
        migrations.RemoveField(
            model_name='match',
            name='player2',
        ),
        migrations.AddField(
            model_name='match',
            name='player2',
            field=models.ManyToManyField(related_name='player2', to='main.Player'),
        ),
    ]
