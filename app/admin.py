from django.contrib import admin
from .models import Project, Toolset, Skill
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['slug', 'link']


class SkillInline(admin.TabularInline):
    model = Skill

@admin.register(Toolset)
class ToolsetAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['toolset', 'name', 'link']