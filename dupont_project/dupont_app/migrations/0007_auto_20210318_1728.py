# Generated by Django 3.1.7 on 2021-03-18 11:58

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dupont_app', '0006_auto_20210318_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]