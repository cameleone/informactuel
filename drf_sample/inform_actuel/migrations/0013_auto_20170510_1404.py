# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_actuel', '0012_auto_20170510_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'permissions': (('commenter_movie', 'Commenter un film'), ('louer_movie', 'Louer des films')), 'ordering': ['code']},
        ),
    ]
