# Generated by Django 2.2 on 2019-08-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Project name', verbose_name='Name')),
                ('mugshot', models.ImageField(upload_to='projects/images/')),
                ('link', models.URLField(help_text='Link to main project')),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Toolset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Program/Language', max_length=50)),
                ('library', models.CharField(blank=True, help_text='Library used', max_length=50, null=True)),
                ('framework', models.CharField(blank=True, help_text='Program framework used', max_length=50, null=True)),
                ('projects', models.ManyToManyField(to='app.Project')),
            ],
        ),
    ]