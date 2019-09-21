# Generated by Django 2.2 on 2019-09-03 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190903_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolset',
            name='skill',
        ),
        migrations.AddField(
            model_name='skill',
            name='toolset',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.Toolset'),
        ),
    ]