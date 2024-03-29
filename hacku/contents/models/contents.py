"""Contents Models."""

# Django
from django.db import models
from django.contrib.postgres.fields import JSONField

# utilities
from hacku.utils.models import HackuModel


class ContentType(models.Model):
    """Content type format."""

    name = models.CharField('Content type name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    def __str__(self):
        """Return content type name."""
        return str(self.name)


class ContentArea(models.Model):
    """Content Area model."""

    name = models.CharField('Content area name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    def __str__(self):
        """Return content area name."""
        return str(self.name)


class Content(HackuModel):
    """Content type format."""

    title = models.TextField(
        'Content Title'
        )

    url = models.URLField(
        'Url Field',
        max_length=500,
        null=True,
        blank=True
    )

    html_content = models.TextField(
        'Html Content',
        null=True,
        blank=True
    )

    content_type = models.ForeignKey(
        'ContentType',
        on_delete=models.CASCADE,
        null=True,
        help_text='Type of content.'
    )

    content_area = models.ForeignKey(
        'ContentArea',
        on_delete=models.CASCADE,
        help_text='Content Area.'
    )

    meta_data = JSONField(
        'Content Metada',
        null=True,
        blank=True
    )

    duration = models.TimeField(
        'Estimated Duration',
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )

    expertise_percentage = models.FloatField(
        'Expertise Percentage',
        default=0
        )

    def __str__(self):
        """Return content title."""
        return str(self.title)

