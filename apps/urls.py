from django.urls import path
from . import views

urlpatterns = [
    path('ResetPasswordLink/<str:uidb64>/<str:token>/', views.reset_password_link, name='ResetPasswordLink'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('<str:load_template>/', views.pages, name='pages'),
]