# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 23:37
from __future__ import unicode_literals

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
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('archive', models.BooleanField(default=False)),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-id'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('duration', models.DurationField(blank=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date', '-id'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Client')),
                ('entries', models.ManyToManyField(to='core.Entry')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('archive', models.BooleanField(default=False)),
                ('estimate', models.DurationField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='core.Client')),
            ],
            options={
                'ordering': ['client', '-id'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='core.Project'),
        ),
        migrations.AddField(
            model_name='entry',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='core.Task'),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL),
        ),
    ]
