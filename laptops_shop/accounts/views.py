# from django.shortcuts import render
# from allauth.account.forms import SignupForm

# class UserLoginView(LoginView):
#     def get_default_redirect_url(self):
#         return reverse("shop:home")


# def logout(request):
#     if request.method == "POST":
#         messages.success(request, "Awesome! You have been logged out successfully!")
#         return LogoutView.as_view(next_page="accounts:login")(request)
#     else:
#         return render(request, "registration/user_logout.html")


# class UserRegistrationView(CreateView):
#     template_name = "registration/registration.html"
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy("shop:home")


# class MyCustomSignupForm(SignupForm):
#     def __init__(self, *args, **kwargs):
#         super(MyCustomSignupForm, self).__init__(*args, **kwargs)
#         self.fields['organization'] = forms.CharField(required=True)
#     def save(self, request):
#         organization = self.cleaned_data.pop('organization')
#         ...
#         user = super(MyCustomSignupForm, self).save(request)