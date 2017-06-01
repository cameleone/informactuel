# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_actuel', '0005_auto_20170504_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='%Y/%m/%d')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='image',
        ),
        migrations.AddField(
            model_name='photo',
            name='movie',
            field=models.ForeignKey(related_name='photos', to='inform_actuel.Movie'),
        ),
    ]
