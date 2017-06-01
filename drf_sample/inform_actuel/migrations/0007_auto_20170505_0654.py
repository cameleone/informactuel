# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_actuel', '0006_auto_20170504_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='movie',
            field=models.ForeignKey(to='inform_actuel.Movie', related_name='photo'),
        ),
    ]
