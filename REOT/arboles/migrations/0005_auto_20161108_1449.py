# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arboles', '0004_auto_20161108_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='altInterCables',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'PD', b'PD'), (b'PE', b'PE'), (b'IA', b'IA')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='altInterLuminarias',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'PD', b'PD'), (b'PE', b'PE'), (b'IA', b'IA')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='inclinacion',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'NO', b'NO'), (b'LI', b'LI'), (b'MI', b'MI')]),
            preserve_default=True,
        ),
    ]
