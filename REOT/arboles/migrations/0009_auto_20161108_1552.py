# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arboles', '0008_arbol_nroarbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='danosAVeredas',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'NO', b'NO'), (b'L', b'L'), (b'I', b'I')]),
            preserve_default=True,
        ),
    ]
