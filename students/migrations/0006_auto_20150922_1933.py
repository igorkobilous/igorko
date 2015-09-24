# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20150922_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0413\u0440\u0443\u043f\u0430', blank=True, to='students.Group', null=True),
        ),
    ]
