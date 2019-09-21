from django.db import models
from django.urls import reverse
# Create your models here.

# Program, Language, Framework, Library and other tools
class Toolset(models.Model):
    name = models.CharField(help_text='Program, Library or Framework', max_length=50, blank=True, null=True)
    link = models.URLField('Official website', default='', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

# Framework, Library of specific languages
class Skill(models.Model):
    toolset = models.ForeignKey(Toolset, on_delete=models.CASCADE, default='')
    name = models.CharField('Language', help_text='Program Language', max_length=50)
    image = models.ImageField(upload_to='skills/images/')
    link = models.URLField(help_text='Visit link')

    class Meta:
        ordering = ['toolset']

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    slug = models.SlugField('Name', help_text='Project name', max_length=50)
    mugshot = models.ImageField(upload_to='projects/images/')
    link = models.URLField(help_text='Link to main project')
    summary = models.TextField()
    toolset = models.ManyToManyField(Toolset)
    STATE = [('Completed', 'Completed'), ('Inprocess', 'Inprocess')]
    status = models.CharField(help_text='State of the project', choices=STATE, max_length=10, default='')

    def __str__(self):
        return f'{self.slug}'
        

    # def get_absolute_url(self):
    #     return reverse('project_detail', kwargs={'slug': self.slug})



