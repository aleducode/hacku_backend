"""Contens models admin."""

# Django
from django.contrib import admin

# Models
from hacku.contents.models import (
    Content,
    ContentArea,
    ContentType
)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    """Content model admin."""

    list_display = ('title', 'url', 'content_type')



@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    """ContentType model admin."""

    list_display = ('name', 'slug_name')


@admin.register(ContentArea)
class ContentAreaAdmin(admin.ModelAdmin):
    """ContentArea model admin."""

    list_display = ('name', 'slug_name')

