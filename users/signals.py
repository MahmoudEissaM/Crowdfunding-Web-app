from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.contrib import messages

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    messages.success(request, f'Welcome back {user.first_name}! You have successfully logged in.')

@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, request, **kwargs):
    messages.error(request, 'Invalid email or password. Please try again.')
