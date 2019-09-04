"""Users views."""

# Django
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth import login

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
    success_url = reverse_lazy('users:complement')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class ThanksView(LoginRequiredMixin, TemplateView):
    """Thanks view."""

    template_name = 'account/thanks.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """logout view."""

    template_name = 'users/logout.html'
