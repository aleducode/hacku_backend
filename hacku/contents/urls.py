"""Contens URLs."""

# Django
from django.urls import path

# Views
from .views import contents

urlpatterns = [
    path(
        route='ver/<int:pk>/',
        view=contents.ContentDetailView.as_view(),
        name='detail'
    ),
    path(
        route='send/',
        view=contents.SendExampleURL.as_view(),
        name='send'
    )
]
