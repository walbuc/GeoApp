# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arboles', '0009_auto_20161108_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='danosAVeredas',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'NO', b'NO'), (b'L', b'L'), (b'I', b'I')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='vereda',
            field=models.CharField(max_length=3, null=True, choices=[(b'PAR', b'PAR'), (b'IMPAR', b'IMPAR')]),
            preserve_default=True,
        ),
    ]
