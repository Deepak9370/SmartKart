from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from .forms import CustomUserCreationForm   # use custom form with email

User = get_user_model()


# -------------------------
# Authentication Views
# -------------------------

def registerview(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
    return render(request, "AuthApp/register.html", {"form": form})


def loginview(request):
    if request.method == "POST":
        u = request.POST.get("un")
        p = request.POST.get("pw")
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            messages.success(request, "Login Successful ✅")
            return redirect("show-phone")
        else:
            messages.error(request, "Invalid Credentials ❌")
    return render(request, "AuthApp/login.html")


def logoutview(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")


# -------------------------
# Password Reset (Function Based)
# -------------------------

def password_reset_request(request):
    """ Step 1: User enters email to get reset link """
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                # Generate reset link properly
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = request.build_absolute_uri(
                    reverse("password_reset_confirm", kwargs={"uidb64": uid, "token": token})
                )

                # Send reset email
                send_mail(
                    "Password Reset Request",
                    f"Hello {user.username},\n\n"
                    f"Click the link below to reset your password:\n{reset_url}\n\n"
                    f"If you did not request this, please ignore this email.",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return redirect("password_reset_done")
            except User.DoesNotExist:
                messages.error(request, "No account found with this email.")
    else:
        form = PasswordResetForm()
    return render(request, "AuthApp/password_reset.html", {"form": form})


def password_reset_confirm(request, uidb64, token):
    """ Step 2: User clicks reset link and sets new password """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect("password_reset_complete")
        else:
            form = SetPasswordForm(user)
        return render(request, "AuthApp/password_reset_confirm.html", {"form": form})
    else:
        messages.error(request, "The password reset link is invalid or has expired ❌")
        return redirect("password_reset")


def password_reset_done(request):
    """ Step 3: Show message after sending email """
    return render(request, "AuthApp/password_reset_done.html")


def password_reset_complete(request):
    """ Step 4: Show success after resetting password """
    return render(request, "AuthApp/password_reset_complete.html")
