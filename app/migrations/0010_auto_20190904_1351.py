# Generated by Django 2.2 on 2019-09-04 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190904_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['toolset']},
        ),
        migrations.AlterModelOptions(
            name='toolset',
            options={'ordering': ['-name']},
        ),
    ]