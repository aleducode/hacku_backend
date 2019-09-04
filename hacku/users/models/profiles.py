"""Profile model."""

# Django
from django.db import models

# utilities
from hacku.utils.models import HackuModel


class ContentType(models.Model):
    """Content type format."""

    name = models.CharField('Content type name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    def __str__(self):
        """Return name name."""
        return str(self.name)


class ContentArea(models.Model):
    """Content Area model."""

    name = models.CharField('Content area name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    def __str__(self):
        """Return name name."""
        return str(self.name)


class PreferenceContentProfile(HackuModel):
    """Preference content model.

    Profile holds a users content data preference
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    content_type = models.ManyToManyField(
        ContentType,
        )
    area = models.ManyToManyField(
        ContentArea,
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
