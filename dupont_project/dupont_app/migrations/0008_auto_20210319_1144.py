# Generated by Django 3.1.7 on 2021-03-19 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dupont_app', '0007_auto_20210318_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_prefer',
            field=models.CharField(choices=[('email', 'Email'), ('phone', 'Phone')], max_length=65),
        ),
    ]