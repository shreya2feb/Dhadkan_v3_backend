# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-10-23 08:45
from __future__ import unicode_literals

import cvd_portal.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_portal', '0003_auto_20201022_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Patient')),
            ],
        ),
    ]
