"""Users views."""

# Django
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.conf import settings

# Forms
from hacku.users.forms import (
    SignUpForm
)
# Twilio
from twilio.rest import Client

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN


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

    def get(self, request, *args, **kwargs):
        user = request.user
        # Twilio
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to='whatsapp:{}'.format(user.phone_number),
            from_='whatsapp:+14155238886',
            body="Hello @{} lets go to learn with HACKU!".format(user.username))
        
        return super().get(request, *args, **kwargs)


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """logout view."""

    template_name = 'users/logout.html'
