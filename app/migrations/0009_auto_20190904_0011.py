# Generated by Django 2.2 on 2019-09-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190903_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolset',
            name='link',
            field=models.URLField(blank=True, default='', null=True, verbose_name='Official website'),
        ),
    ]
