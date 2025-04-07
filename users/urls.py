from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
