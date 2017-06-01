# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_actuel', '0002_auto_20170503_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realisateur',
            name='date_naissance_real',
            field=models.DateField(),
        ),
    ]
