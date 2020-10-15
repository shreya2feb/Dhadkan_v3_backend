# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-10-06 15:07
from __future__ import unicode_literals

import cvd_portal.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, default='', max_length=20)),
                ('device_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Somesh', max_length=60)),
                ('hospital', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField(blank=True)),
                ('speciality', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('device', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='cvd_portal.Device')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('byte', models.TextField()),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('user_type', models.TextField()),
                ('user_type_id', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Somesh', max_length=60)),
                ('date_of_birth', models.IntegerField(blank=True)),
                ('gender', models.IntegerField(default=1)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.TextField(null=True)),
                ('mobile', models.BigIntegerField(blank=True)),
                ('device', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='cvd_portal.Device')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='cvd_portal.Doctor')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic', models.IntegerField()),
                ('diastolic', models.IntegerField(default=0)),
                ('weight', models.IntegerField()),
                ('heart_rate', models.IntegerField()),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='cvd_portal.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientData2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
                ('ques1', models.IntegerField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data2', to='cvd_portal.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time', cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now)),
                ('repeat', models.BooleanField(default=True)),
                ('frequency', models.FloatField(default=1.0)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='notifications',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Patient'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Patient'),
        ),
        migrations.AddField(
            model_name='image',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='cvd_portal.Patient'),
        ),
    ]