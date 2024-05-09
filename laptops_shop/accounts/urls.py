from django.urls import path
from accounts.views import UserLoginView, UserRegistrationView
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),
    path("registration/", UserRegistrationView.as_view(), name="registration"
    ),
]
