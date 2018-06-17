# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-16 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='出勤时间')),
                ('end_time', models.DateTimeField(verbose_name='退勤时间')),
                ('rest_time', models.SmallIntegerField(verbose_name='休息时间')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
            options={
                'verbose_name': '考勤',
                'verbose_name_plural': '考勤',
                'db_table': 'yo_attendances',
            },
        ),
    ]
