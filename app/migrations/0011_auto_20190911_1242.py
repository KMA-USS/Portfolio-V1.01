# Generated by Django 2.2 on 2019-09-11 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190904_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toolset',
            options={'ordering': ['name']},
        ),
    ]