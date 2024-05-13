from django.urls import path
from accounts.views import UserLoginView, UserRegistrationView, logout, google_login


app_name = "accounts"

urlpatterns = [
    # path("login/", UserLoginView.as_view(), name="login"),
    # path("logout/", logout, name="logout"),
    # path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("login/google/", google_login, name="google_login"),
]
