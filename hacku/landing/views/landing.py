"""Landing views."""

# Django
from django.views.generic import  TemplateView


class IndexView(TemplateView):
    """Landing principal view."""

    template_name = 'landing/index.html' 