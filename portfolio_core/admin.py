from django.contrib import admin
from .models import Achievement, Project, Skill

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'year', 'category', 'order')
    list_editable = ('order',)
    list_filter = ('category', 'year')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'date', 'order')
    list_editable = ('order',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'energy', 'order')
    list_editable = ('order', 'energy')
