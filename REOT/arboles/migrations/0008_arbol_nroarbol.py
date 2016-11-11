# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arboles', '0007_auto_20161108_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='arbol',
            name='nroArbol',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
