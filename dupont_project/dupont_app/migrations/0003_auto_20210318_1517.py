# Generated by Django 3.1.7 on 2021-03-18 09:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('dupont_app', '0002_auto_20210318_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinelearningmodelreference',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='researchupdates',
            name='blog_desc',
            field=tinymce.models.HTMLField(),
        ),
    ]