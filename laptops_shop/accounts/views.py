from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


from accounts.forms import UserRegistrationForm


class UserLoginView(LoginView):
    def get_default_redirect_url(self):
        return reverse("shop:home")


def logout(request):
    if request.method == "POST":
        messages.success(request, "Awesome! You have been logged out successfully!")
        return LogoutView.as_view(next_page="accounts:login")(request)
    else:
        return render(request, "registration/user_logout.html")


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("shop:home")
