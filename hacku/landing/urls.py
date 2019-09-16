"""Landing URLs."""

# Django
from django.urls import path

# Views
from .views import landing as landing_views

urlpatterns = [
    path(
        route='',
        view=landing_views.IndexView.as_view(),
        name='index'
    ),
    
]
