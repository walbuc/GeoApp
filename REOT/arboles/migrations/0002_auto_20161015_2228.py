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
            name='imagen',
            field=models.FileField(upload_to=b'uploads/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='arbol',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'fecha de publicacion'),
            preserve_default=True,
        ),
    ]
