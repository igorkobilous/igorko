# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stud_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stprofile',
            name='address',
            field=models.CharField(default=b'', max_length=256, verbose_name='Adress', blank=True),
        ),
        migrations.AddField(
            model_name='stprofile',
            name='student_card',
            field=models.CharField(default=b'', max_length=10, verbose_name='Student Card', blank=True),
        ),
    ]
