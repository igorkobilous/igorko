# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20160205_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='first_name_en',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name_pl',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name_uk',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name_en',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name_pl',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name_uk',
        ),
        migrations.RemoveField(
            model_name='student',
            name='middle_name_en',
        ),
        migrations.RemoveField(
            model_name='student',
            name='middle_name_pl',
        ),
        migrations.RemoveField(
            model_name='student',
            name='middle_name_uk',
        ),
        migrations.RemoveField(
            model_name='student',
            name='notes_en',
        ),
        migrations.RemoveField(
            model_name='student',
            name='notes_pl',
        ),
        migrations.RemoveField(
            model_name='student',
            name='notes_uk',
        ),
    ]
