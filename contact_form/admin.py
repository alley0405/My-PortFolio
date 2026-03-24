from django.contrib import admin
from .models import ContactQuery

@admin.register(ContactQuery)
class ContactQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'created_at')
    search_fields = ('name', 'email', 'project_details')
