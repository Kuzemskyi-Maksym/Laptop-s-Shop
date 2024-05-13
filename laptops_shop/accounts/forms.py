from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from allauth.account.adapter import DefaultAccountAdapter


class UserRegistrationForm(UserCreationForm):
    email = EmailField(max_length=200, help_text="Please use your working email")

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def signup(self, request, user):
        # Perform any additional actions you want to happen during signup
        # (e.g., sending a welcome email, saving additional profile data)
        user.save()  # Save the user to the database
