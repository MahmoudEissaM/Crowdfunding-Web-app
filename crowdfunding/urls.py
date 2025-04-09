from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import LogoutView
from users.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', logout_view, name='account_logout'),  # Override allauth logout
    path('accounts/', include('allauth.urls')),
    path('', include('users.urls')),
    path('projects/', include('projects.urls', namespace='projects')),  # ✅ Correct include
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)