# Generated by Django 2.2.4 on 2019-09-10 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferencecontentprofile',
            name='expertise_percentage',
            field=models.FloatField(default=0, verbose_name='Expertise Percentage'),
        ),
    ]
