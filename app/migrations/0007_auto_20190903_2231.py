# Generated by Django 2.2 on 2019-09-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_toolset_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Program Language', max_length=50, verbose_name='Language')),
                ('image', models.ImageField(upload_to='skills/images/')),
                ('link', models.URLField(help_text='Visit link')),
            ],
        ),
        migrations.AddField(
            model_name='toolset',
            name='skill',
            field=models.ManyToManyField(to='app.Skill'),
        ),
    ]