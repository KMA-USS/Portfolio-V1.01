# Generated by Django 2.2 on 2019-09-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190831_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolset',
            name='link',
            field=models.URLField(default='', verbose_name='Official website'),
        ),
    ]
