# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arboles', '0010_auto_20161108_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arbol',
            options={'verbose_name_plural': 'Arboles'},
        ),
        migrations.AlterField(
            model_name='arbol',
            name='nroFrente',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='vereda',
            field=models.CharField(max_length=3, null=True, choices=[(b'NO', b'NO'), (b'PAR', b'PAR'), (b'IMPAR', b'IMPAR')]),
            preserve_default=True,
        ),
    ]
