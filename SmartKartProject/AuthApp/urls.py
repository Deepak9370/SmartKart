from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerview, name="register"),
    path("login/", views.loginview, name="login"),
    path("logout/", views.logoutview, name="logout"),

    # Password Reset URLs
    path("password-reset/", views.password_reset_request, name="password_reset"),
    path("password-reset/done/", views.password_reset_done, name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.password_reset_confirm, name="password_reset_confirm"),
    path("reset/done/", views.password_reset_complete, name="password_reset_complete"),
]
