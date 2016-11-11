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
                ('especie', models.CharField(max_length=200, blank=True)),
                ('estadoSanitario', models.CharField(max_length=1, blank=True)),
                ('inclinacion', models.FloatField(blank=True)),
                ('ahuecamiento', models.FloatField(blank=True)),
                ('altInterCables', models.CharField(max_length=2, blank=True)),
                ('altInterLuminarias', models.CharField(max_length=2, blank=True)),
                ('danosAMuros', models.CharField(blank=True, max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('danosAVeredas', models.CharField(max_length=2, blank=True)),
                ('cazuela', models.CharField(max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('tipoDeTransito', models.CharField(blank=True, max_length=10, choices=[(b'PESADO', b'PESADO'), (b'PARTICULAR', b'PARTICULAR')])),
                ('distanciaEntrePlantas', models.FloatField(blank=True)),
                ('distanciaAlMuro', models.FloatField(blank=True)),
                ('podasAnteriores', models.CharField(max_length=2, blank=True)),
                ('circunferencia', models.IntegerField(blank=True)),
                ('observaciones', models.CharField(max_length=400, blank=True)),
                ('latitud', models.CharField(max_length=200, verbose_name=b'Latitud')),
                ('longitud', models.CharField(max_length=400, verbose_name=b'Longitud')),
                ('imagen1', models.FileField(upload_to=b'uploads/')),
                ('imagen2', models.FileField(upload_to=b'uploads/', blank=True)),
                ('imagen3', models.FileField(upload_to=b'uploads/', blank=True)),
                ('imagen4', models.FileField(upload_to=b'uploads/', blank=True)),
                ('imagen5', models.FileField(upload_to=b'uploads/', blank=True)),
                ('imagen6', models.FileField(upload_to=b'uploads/', blank=True)),
                ('imagen7', models.FileField(upload_to=b'uploads/', blank=True)),
                ('imagen8', models.FileField(upload_to=b'uploads/', blank=True)),
                ('imagen9', models.FileField(upload_to=b'uploads/', blank=True)),
                ('imagen10', models.FileField(upload_to=b'uploads/', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de publicacion')),
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
