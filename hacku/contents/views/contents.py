"""Content views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import login

# Models
from hacku.contents.models import Content
from hacku.users.models import User

# Utils
import jwt
from datetime import timedelta

# Twilio
from twilio.rest import Client


def gen_verification_token(user):
    """Create JWT token that the user can use to see the content."""
    expiration_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.username,
        # UTC format
        'exp': int(expiration_date.timestamp()),
        'type': 'content_login'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode()


class ContentDetailView(LoginRequiredMixin, DetailView):
    """Content detail view."""

    template_name = 'account/content_viewer.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = Content.objects.all()
    context_object_name = 'content'

    def dispatch(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        token = self.request.GET.get('token')
        # TODO: Handle expire token and bad request
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        # Force login
        user = User.objects.get(username=payload.get('user'))
        login(self.request, user)
        return super().dispatch(request, *args, **kwargs)


class SendExampleURL(LoginRequiredMixin, TemplateView):
    """Send url content example."""
    
    template_name = 'account/thanks.html'
    
    def get(self, request, *args, **kwargs):
        user = self.request.user
        verification_token = gen_verification_token(user)
        url = reverse_lazy('contents:detail', kwargs={'pk': '1'})
        complete_url = '{}/contents/ver/1?token={}'.format(
            'localhost:8000',
            verification_token)
        # account_sid = "ACee4d3b631b78711699fddf9ec2f52824"
        # # Your Auth Token from twilio.com/console
        # auth_token = "32c89246ef729ecfb52b789a3a81313a"
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #         to='whatsapp:{}'.format(user.phone_number),
        #         from_='whatsapp:+14155238886',
        #         body='hi @{} this is your daily capsule {}'.format(
        #             user.username,
        #             str(complete_url)
        #             ))
        print(complete_url)
        return super().get(request, *args, **kwargs)



