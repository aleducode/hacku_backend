"""Users URLs."""

# Django
from django.urls import path

# Views
from .views import users as users_views
from .views import profiles as profiles_views

urlpatterns = [
    # Management
    path(
        route='login/',
        view=users_views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='',
        view=users_views.SignupView.as_view(),
        name='signup'
    ),
    # path(
    #     route='me/profile/',
    #     view=views.UpdateProfile.as_view(),
    #     name='update_profile'
    # ),
    # path(
    #     route='<str:username>/',
    #     view=views.UserDetailView.as_view(),
    #     name='detail'
    # )
]
