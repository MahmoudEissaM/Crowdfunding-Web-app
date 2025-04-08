from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path
from homepage import views  # Import views from the correct app

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'frontend/build/static']

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('homepage.urls')),  # Include homepage URLs
    path('api/top-rated-projects/', views.top_rated_projects, name='top-rated-projects'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
