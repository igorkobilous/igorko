# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20160113_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['subject'], 'verbose_name': 'Exam', 'verbose_name_plural': 'Exams'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title'], 'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
        migrations.AlterModelOptions(
            name='monthjournal',
            options={'verbose_name': 'Month Journal', 'verbose_name_plural': 'Month Journals'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name'], 'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AddField(
            model_name='student',
            name='first_name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name_pl',
            field=models.CharField(max_length=256, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name_uk',
            field=models.CharField(max_length=256, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name_pl',
            field=models.CharField(max_length=256, null=True, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name_uk',
            field=models.CharField(max_length=256, null=True, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name_en',
            field=models.CharField(default=b'', max_length=256, null=True, verbose_name='Middle Name', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name_pl',
            field=models.CharField(default=b'', max_length=256, null=True, verbose_name='Middle Name', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name_uk',
            field=models.CharField(default=b'', max_length=256, null=True, verbose_name='Middle Name', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='notes_en',
            field=models.TextField(null=True, verbose_name='Additional note', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='notes_pl',
            field=models.TextField(null=True, verbose_name='Additional note', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='notes_uk',
            field=models.TextField(null=True, verbose_name='Additional note', blank=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateField(verbose_name='Date', blank=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='lecturer',
            field=models.CharField(max_length=256, verbose_name='Lecturer'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='notes',
            field=models.TextField(verbose_name='Additional note', blank=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.CharField(max_length=256, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Student', verbose_name='Leader'),
        ),
        migrations.AlterField(
            model_name='group',
            name='notes',
            field=models.TextField(verbose_name='Additional note', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='student',
            field=models.ForeignKey(unique_for_month=b'date', verbose_name='Student', to='students.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default=b'', max_length=256, verbose_name='Middle Name', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(verbose_name='Additional note', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='Photo', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(max_length=256, verbose_name='Ticket'),
        ),
    ]
