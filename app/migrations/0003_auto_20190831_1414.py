# Generated by Django 2.2 on 2019-08-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_project_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolset',
            name='projects',
        ),
        migrations.AddField(
            model_name='project',
            name='toolset',
            field=models.ManyToManyField(to='app.Toolset'),
        ),
    ]
