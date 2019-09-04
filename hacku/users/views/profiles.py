"""Profiles views."""

# Django
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

# Form
from hacku.users.forms import (
    PreferenceContentProfileForm
)


class PreferenceContentProfileView(LoginRequiredMixin, FormView):
    """Users Sign Up View."""

    template_name = 'account/preference_concept.html'
    form_class = PreferenceContentProfileForm
    success_url = reverse_lazy('users:thanks')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)