from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import user_signup, user_login, user_profile


app_name = "accounts"

urlpatterns = [
    path("user-registration/", user_signup, name="registration"),
    path("user-login/", user_login, name="login"),
    path("user-logout/", LogoutView.as_view(), name="logout"),
    path('user-profile/', user_profile, name="profile")
]
