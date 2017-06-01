# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_actuel', '0010_movie_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(default='LONG METRAGE', choices=[('LONG METRAGE', 'Long metrage'), ('SERIE', 'Serie')], max_length=3),
        ),
    ]
