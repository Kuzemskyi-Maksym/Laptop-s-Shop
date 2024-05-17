from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
# from django.contrib import messages
from .forms import SignUpForm, LoginForm


def user_signup(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():  # Call is_valid() here
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                form.save()
                new_user = authenticate(username=username, password=password)
                if new_user is not None:
                    login(request, new_user)
                    # messages.success(request, f"Thank you for registering, {username}.")
                    return redirect("shop:home")
    # else:
    #     return redirect("accounts:logout")
    form = SignUpForm()
    context = {"title": "SignUp", "form": form}
    return render(request, "registration/signup.html", context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("shop:home")
    else:
        form = LoginForm()

    context = {"title": "SignIn", "form": form}

    return render(request, "registration/login.html", context)


def user_profile(request):

    context = {
        "title": "Account",
    }
    return render(request, "registration/user_profile.html", context)

def user_profile_change(request):

    context = {
        "title": "Change account",
    }
    return render(request, 'registration/user_profile_change.html', context)