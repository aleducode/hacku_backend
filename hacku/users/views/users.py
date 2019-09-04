"""Users views."""

# Django
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

# Forms
from hacku.users.forms import (
    SignUpForm
)


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'account/login.html'


class SignupView(FormView):
    """Users Sign Up View."""

    template_name = 'account/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:create-profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
