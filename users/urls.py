from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

STATIC_URL = '/static/'
STATICFILES_DIRS = [settings.BASE_DIR / 'frontend/build/static']

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=11,
        unique=True
    )
    profile_picture = models.ImageField(upload_to='profile_pics/')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             success_url='/password-reset-complete/'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/top-rated-projects/', views.top_rated_projects, name='top-rated-projects'),
    path('api/latest-projects/', views.latest_projects, name='latest-projects'),
    path('api/featured-projects/', views.featured_projects, name='featured-projects'),
    path('api/categories/', views.categories, name='categories'),
]
