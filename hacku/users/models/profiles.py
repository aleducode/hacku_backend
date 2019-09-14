"""Profile model."""

# Django
from django.db import models

# utilities
from hacku.utils.models import HackuModel
from django.contrib.postgres.fields import JSONField


class PreferenceContentProfile(HackuModel):
    """Preference content model.

    Profile holds a users content data preference
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    content_type = models.ManyToManyField(
        'contents.ContentType',
    )
    area = models.ManyToManyField(
        'contents.ContentArea',
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

    expertise_percentage = models.FloatField(
        'Expertise Percentage',
        default=0
    )

    meta_data = JSONField(
        'Profile Preference Metada',
        null=True,
        blank=True
    )

    def __str__(self):
        """Return users name."""
        return str(self.user)
