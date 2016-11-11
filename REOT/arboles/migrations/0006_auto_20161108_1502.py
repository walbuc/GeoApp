# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arboles', '0005_auto_20161108_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='circunferencia',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
