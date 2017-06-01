# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_actuel', '0008_auto_20170505_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='photo',
            field=models.ImageField(upload_to='photos/', null=True),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
