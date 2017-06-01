# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_actuel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acteur',
            name='date_naissance_act',
            field=models.DateField(),
        ),
    ]
