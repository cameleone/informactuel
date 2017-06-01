# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inform_actuel', '0011_auto_20170505_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('Adresse', models.CharField(blank=True, max_length=255)),
                ('avatar', models.ImageField(null=True, blank=True, upload_to='avatars/')),
                ('telephone', models.CharField(blank=True, max_length=25)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(choices=[('LONG METRAGE', 'Long metrage'), ('SERIE', 'Serie')], default='LONG METRAGE', max_length=15),
        ),
    ]
