from django import views
from django.urls import path
from django.views.generic.base import TemplateView
from .views import register
from django.contrib.auth import views
urlpatterns = [
    # These paths comes from path('accounts/', include('django.contrib.auth.urls')) 
    # and if you want to modify or want to see what have been done at the backend,you can go to definitions
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ), 
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home'),




    path('accounts/register', register,name="register"),



]
