"""Profile model."""

# Django
from django.db import models

# utilities
from hacku.utils.models import HackuModel


class ContentType(models.Model):
    """Content type format."""

    name = models.CharField('Content type name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)


class PreferenceContentProfile(HackuModel):
    """Preference content model.

    Profile holds a users content data preference
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    content_type = models.ForeignKey(
        'profiles.ContentType',
        on_delete=models.SET_NULL,
        null=True
        )

    hour = models.TimeField(
        'Hour preference',
        auto_now=False,
        auto_now_add=False
    )

    english_content = models.BooleanField(
        'English Content',
        default=False,
        help_text='Used for enable english content.'
    )

    def __str__(self):
        """Return users name."""
        return str(self.user)
