# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_actuel', '0009_auto_20170505_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='type',
            field=models.CharField(default='LM', choices=[('LM', 'Long metrage'), ('SR', 'Serie')], max_length=3),
        ),
    ]
