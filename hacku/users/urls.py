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
        route='logout/',
        view=users_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='',
        view=users_views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='complement/',
        view=profiles_views.PreferenceContentProfileView.as_view(),
        name='complement'
    ),
    path(
        route='thanks/',
        view=users_views.ThanksView.as_view(),
        name='thanks'
    ),
    # path(
    #     route='<str:username>/',
    #     view=views.UserDetailView.as_view(),
    #     name='detail'
    # )
]
