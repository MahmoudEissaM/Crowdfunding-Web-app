from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from .forms import CustomUserCreationForm
from .tokens import account_activation_token
from .models import User  
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            context = {
                'user': user,
                'domain': request.get_host(),  # This will get the correct domain with port
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'protocol': 'http' if not request.is_secure() else 'https'
            }
            message = render_to_string('users/activation_email.html', context)
            email = EmailMessage(mail_subject, message, to=[user.email])
            email.content_subtype = "html"
            email.send()
            
            return render(request, 'users/email_verification_sent.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated successfully! You can now login.')
        return render(request, 'users/activation_success.html')
    else:
        return render(request, 'users/activation_invalid.html')

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Request"
                    email_template_name = "users/password_reset_email.html"
                    context = {
                        "user": user,
                        'domain': request.get_host(),
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http' if not request.is_secure() else 'https',
                    }
                    email = render_to_string(email_template_name, context)
                    try:
                        send_mail(
                            subject,
                            email,
                            'Crowdfunding Support <support@crowdfunding.com>',
                            [user.email],
                            fail_silently=False
                        )
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, "Password reset instructions have been sent to your email.")
                    return redirect("password_reset_done")
            messages.error(request, "No user found with this email address.")
    password_reset_form = PasswordResetForm()
    return render(request, "users/password_reset.html", {"form": password_reset_form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, f'Welcome back {user.first_name}!')
                return redirect('dashboard')  # Redirect to dashboard after login
            else:
                messages.error(request, 'Please verify your email first.')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'users/login.html')

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html', {
        'user': request.user
    })
