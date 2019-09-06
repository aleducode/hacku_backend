"""Main Hacku URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    # Other app
    path('', include(('hacku.users.urls', 'users'), namespace='users')),
    path('contents/', include(('hacku.contents.urls', 'contents'), namespace='contents')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
