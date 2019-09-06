"""Contens models admin."""

# Django
from django.contrib import admin

# Models
from hacku.contents.models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    """Content model admin."""

    list_display = ('title', 'url', 'content_type')
