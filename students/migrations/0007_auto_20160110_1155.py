# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20150922_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u0434\u0430\u0442\u0430')),
                ('present_day1', models.BooleanField(default=False)),
                ('present_day2', models.BooleanField(default=False)),
                ('present_day3', models.BooleanField(default=False)),
                ('present_day4', models.BooleanField(default=False)),
                ('present_day5', models.BooleanField(default=False)),
                ('present_day6', models.BooleanField(default=False)),
                ('present_day7', models.BooleanField(default=False)),
                ('present_day8', models.BooleanField(default=False)),
                ('present_day9', models.BooleanField(default=False)),
                ('present_day10', models.BooleanField(default=False)),
                ('present_day11', models.BooleanField(default=False)),
                ('present_day12', models.BooleanField(default=False)),
                ('present_day13', models.BooleanField(default=False)),
                ('present_day14', models.BooleanField(default=False)),
                ('present_day15', models.BooleanField(default=False)),
                ('present_day16', models.BooleanField(default=False)),
                ('present_day17', models.BooleanField(default=False)),
                ('present_day18', models.BooleanField(default=False)),
                ('present_day19', models.BooleanField(default=False)),
                ('present_day20', models.BooleanField(default=False)),
                ('present_day21', models.BooleanField(default=False)),
                ('present_day22', models.BooleanField(default=False)),
                ('present_day23', models.BooleanField(default=False)),
                ('present_day24', models.BooleanField(default=False)),
                ('present_day25', models.BooleanField(default=False)),
                ('present_day26', models.BooleanField(default=False)),
                ('present_day27', models.BooleanField(default=False)),
                ('present_day28', models.BooleanField(default=False)),
                ('present_day29', models.BooleanField(default=False)),
                ('present_day30', models.BooleanField(default=False)),
                ('present_day31', models.BooleanField(default=False)),
                ('student', models.ForeignKey(unique_for_month=b'date', verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student')),
            ],
            options={
                'verbose_name': '\u041c\u0456\u0441\u044f\u0447\u043d\u0438\u0439 \u0436\u0443\u0440\u043d\u0430\u043b',
                'verbose_name_plural': '\u041c\u0456\u0441\u044f\u0447\u043d\u0456 \u0436\u0443\u0440\u043d\u0430\u043b\u0438',
            },
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['subject'], 'verbose_name': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d', 'verbose_name_plural': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d\u0438'},
        ),
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0456 \u0447\u0430\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0413\u0440\u0443\u043f\u0430', to='students.Group', null=True),
        ),
    ]
