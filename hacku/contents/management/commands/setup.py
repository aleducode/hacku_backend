"""Setup Command."""

# Django
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Setup base command."""

    def handle(self, *args, **options):
        """Handle command usage."""
        call_command('migrate')
        call_command('loaddata',
                     'contentarea',
                     'contenttype')
        self.stdout.write(self.style.SUCCESS('OK'))
