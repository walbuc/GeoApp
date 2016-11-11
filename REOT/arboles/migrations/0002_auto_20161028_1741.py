# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arboles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='ahuecamiento',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='altInterCables',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='altInterLuminarias',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='circunferencia',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='danosAMuros',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'SI', b'SI'), (b'NO', b'NO')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='danosAVeredas',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='distanciaAlMuro',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='distanciaEntrePlantas',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='especie',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='estadoSanitario',
            field=models.CharField(max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen10',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen2',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen3',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen4',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen5',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen6',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen7',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen8',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen9',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='inclinacion',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='observaciones',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='podasAnteriores',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de publicacion', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='tipoDeTransito',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'PESADO', b'PESADO'), (b'PARTICULAR', b'PARTICULAR')]),
            preserve_default=True,
        ),
    ]
