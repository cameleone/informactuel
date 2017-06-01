# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acteur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('code_act', models.CharField(max_length=10, unique=True)),
                ('nom_act', models.CharField(max_length=50)),
                ('prenom_act', models.CharField(max_length=150)),
                ('date_naissance_act', models.IntegerField(default=3)),
                ('gender_act', models.CharField(max_length=3, default='MR', choices=[('MR', 'Monsieur'), ('MME', 'Madame')])),
            ],
            options={
                'ordering': ['nom_act'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('code_gen', models.CharField(max_length=6, unique=True)),
                ('description_gen', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['description_gen'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(max_length=10, blank=True, unique=True, null=True)),
                ('titre', models.CharField(max_length=100)),
                ('resume', models.TextField()),
                ('duree', models.CharField(max_length=10)),
                ('url_trailer', models.URLField(blank=True, null=True)),
                ('date_sortie', models.DateField()),
                ('exclu', models.BooleanField()),
                ('url_detail', models.URLField(blank=True, null=True)),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now)),
                ('acteurs', models.ManyToManyField(to='inform_actuel.Acteur', related_name='Movie')),
                ('genre', models.ForeignKey(to='inform_actuel.Genre')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Realisateur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('code_real', models.CharField(max_length=10, unique=True)),
                ('nom_real', models.CharField(max_length=50)),
                ('prenom_real', models.CharField(max_length=150)),
                ('date_naissance_real', models.IntegerField(default=3)),
                ('gender_real', models.CharField(max_length=3, default='MR', choices=[('MR', 'Monsieur'), ('MME', 'Madame')])),
            ],
            options={
                'ordering': ['nom_real'],
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='realisateurs',
            field=models.ManyToManyField(to='inform_actuel.Realisateur', related_name='Movie'),
        ),
    ]
