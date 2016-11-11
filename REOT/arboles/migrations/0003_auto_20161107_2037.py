# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arboles', '0002_auto_20161028_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='arbol',
            name='anchoVereda',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arbol',
            name='calle',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arbol',
            name='vereda',
            field=models.CharField(max_length=2, null=True, choices=[(b'PAR', b'PAR'), (b'IMPAR', b'IMPAR')]),
            preserve_default=True,
        ),
    ]
