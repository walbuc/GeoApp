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
                ('calle', models.CharField(max_length=200, null=True, blank=True)),
                ('anchoVereda', models.FloatField(null=True, blank=True)),
                ('vereda', models.CharField(max_length=3, null=True, choices=[(b'NO', b'NO'), (b'PAR', b'PAR'), (b'IMPAR', b'IMPAR')])),
                ('nroFrente', models.IntegerField(null=True, blank=True)),
                ('nroArbol', models.IntegerField()),
                ('especie', models.CharField(max_length=200, null=True, blank=True)),
                ('estadoSanitario', models.CharField(blank=True, max_length=1, null=True, choices=[(b'S', b'S'), (b'D', b'D'), (b'M', b'M')])),
                ('inclinacion', models.CharField(blank=True, max_length=2, null=True, choices=[(b'NO', b'NO'), (b'LI', b'LI'), (b'MI', b'MI')])),
                ('ahuecamiento', models.CharField(max_length=10, null=True, blank=True)),
                ('altInterCables', models.CharField(blank=True, max_length=2, null=True, choices=[(b'PD', b'PD'), (b'PE', b'PE'), (b'IA', b'IA')])),
                ('altInterLuminarias', models.CharField(blank=True, max_length=2, null=True, choices=[(b'PD', b'PD'), (b'PE', b'PE'), (b'IA', b'IA')])),
                ('danosAMuros', models.CharField(blank=True, max_length=2, null=True, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('danosAVeredas', models.CharField(blank=True, max_length=2, null=True, choices=[(b'NO', b'NO'), (b'L', b'L'), (b'I', b'I')])),
                ('cazuela', models.CharField(max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('tipoDeTransito', models.CharField(blank=True, max_length=10, null=True, choices=[(b'PESADO', b'PESADO'), (b'PARTICULAR', b'PARTICULAR')])),
                ('distanciaEntrePlantas', models.FloatField(null=True, blank=True)),
                ('distanciaAlMuro', models.FloatField(null=True, blank=True)),
                ('podasAnteriores', models.CharField(blank=True, max_length=2, null=True, choices=[(b'NO', b'NO'), (b'L', b'L'), (b'S ', b'S')])),
                ('circunferencia', models.FloatField(null=True, blank=True)),
                ('observaciones', models.CharField(max_length=400, null=True, blank=True)),
                ('latitud', models.CharField(max_length=200, verbose_name=b'Latitud')),
                ('longitud', models.CharField(max_length=400, verbose_name=b'Longitud')),
                ('imagen1', models.FileField(upload_to=b'uploads/')),
                ('imagen2', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('imagen3', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('imagen4', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('imagen5', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('imagen6', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('imagen7', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('imagen8', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('imagen9', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('imagen10', models.FileField(null=True, upload_to=b'uploads/', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de publicacion', null=True)),
            ],
            options={
                'verbose_name_plural': 'Arboles',
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
