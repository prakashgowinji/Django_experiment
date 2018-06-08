# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 07:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=60)),
                ('price', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarian', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Library'),
        ),
    ]
