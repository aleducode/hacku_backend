# Generated by Django 2.2.4 on 2019-09-10 12:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='meta_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Content Metada'),
        ),
    ]
