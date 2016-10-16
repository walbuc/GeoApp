# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arbol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nroFrente', models.IntegerField()),
                ('especie', models.CharField(max_length=200)),
                ('estadoSanitario', models.CharField(max_length=1)),
                ('inclinacion', models.FloatField()),
                ('ahuecamiento', models.FloatField()),
                ('altInterCables', models.CharField(max_length=2)),
                ('altInterLuminarias', models.CharField(max_length=2)),
                ('danosAMuros', models.CharField(max_length=2)),
                ('danosAVeredas', models.CharField(max_length=2)),
                ('cazuela', models.CharField(max_length=200)),
                ('distanciaEntrePlantas', models.FloatField()),
                ('distanciaAlMuro', models.FloatField()),
                ('podasAnteriores', models.CharField(max_length=2)),
                ('circunferencia', models.IntegerField()),
                ('observaciones', models.CharField(max_length=400)),
                ('latitud', models.CharField(max_length=200)),
                ('longitud', models.CharField(max_length=400)),
                ('imagen', models.FileField(upload_to=b'uploads')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Censista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='arbol',
            name='censista',
            field=models.ForeignKey(to='arboles.Censista'),
            preserve_default=True,
        ),
    ]
