# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20150915_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='two_name',
            field=models.CharField(default=b'', max_length=256, verbose_name="\u0414\u0440\u0443\u0433\u0435 \u0456\u043c'\u044f", blank=True),
        ),
    ]
