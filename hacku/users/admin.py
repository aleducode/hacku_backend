"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from hacku.users.models import (
    User,
    PreferenceContentProfile,
    )


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_staff', 'is_client', 'created')


@admin.register(PreferenceContentProfile)
class PreferenceContentProfileAdmin(admin.ModelAdmin):
    """PreferenceContentProfile model admin."""

    list_display = ('user', 'hour', 'expertise_percentage')
    search_fields = ('user__username', 'user__email', 'user___first_name', 'user__last_name')


admin.site.register(User, CustomUserAdmin)
