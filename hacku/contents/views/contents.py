"""Content views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import login
from django.shortcuts import render
# Models
from hacku.contents.models import Content
from hacku.users.models import User

# Utils
import jwt
from datetime import timedelta

# Twilio
from twilio.rest import Client
account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN


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
        token = self.request.GET.get('token', None)
        # TODO: Handle expire token and bad request
        if token:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            # Force login
            user = User.objects.get(username=payload.get('user'))
            login(self.request, user)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Percentage expertise creation."""
        # TODO: kill token vigence or viewed publications by user
        expertise_percentage_selected = int(request.POST.get('expertise_percentage'))
        user = self.request.user
        publication = self.get_object()
        # expertise date
        user_expertise = user.preferencecontentprofile.expertise_percentage
        publication_expertise = publication.expertise_percentage

        if expertise_percentage_selected >= 50:
            user_expertise += 0.05*publication_expertise
        elif expertise_percentage_selected in range(5, 50):
            user_expertise += 0.02*publication_expertise
        else:
            user_expertise -= 0.05*publication_expertise

        # considerable expert calification
        if user_expertise > 50:
            diff = (publication_expertise - expertise_percentage_selected)
            if diff not in range(-20, 20):
                if diff > 0:
                    # add expertise to publication
                    publication_expertise += 10
                else:
                    # less expertise to publication
                    publication_expertise -= 10
        user.preferencecontentprofile.expertise_percentage = user_expertise
        user.preferencecontentprofile.save()
        publication.expertise_percentage = publication_expertise
        publication.save()
        return render(request, 'account/feedback.html')


class SendExampleURL(LoginRequiredMixin, TemplateView):
    """Send url content example."""

    template_name = 'account/sent_test.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        verification_token = gen_verification_token(user)
        complete_url = '{}/contents/ver/1?token={}'.format(
            settings.URL_HACKU,
            verification_token)

        client = Client(account_sid, auth_token)
        message = client.messages.create(
                to='whatsapp:{}'.format(user.phone_number),
                from_='whatsapp:+14155238886',
                body='hi @{} this is your daily capsule {}'.format(
                    user.username,
                    str(complete_url)
                    ))
        return super().get(request, *args, **kwargs)



