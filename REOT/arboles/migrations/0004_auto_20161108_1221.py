# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arboles', '0003_auto_20161107_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='ahuecamiento',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='danosAVeredas',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'NO', b'NO'), (b'L', b'L'), (b'I', b'I')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='estadoSanitario',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'S', b'S'), (b'D', b'D'), (b'M', b'M')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='inclinacion',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='podasAnteriores',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'NO', b'NO'), (b'L', b'L'), (b'S ', b'S')]),
            preserve_default=True,
        ),
    ]
