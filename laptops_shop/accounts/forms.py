import email
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "required": "",
                "name": "username",
                "id": "username",
                "type": "text",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "placeholder": "Username",
                "style": "height: 50px !important; margin-top: 20px !important;",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "required": "",
                "name": "email",
                "id": "email",
                "type": "email",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "placeholder": "Email",
                "style": "height: 50px !important; margin-top: -20px !important;",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "required": "",
                "name": "password",
                "id": "password1",
                "type": "password",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "placeholder": "Password",
                "style": "height: 50px !important; margin-top: 20px !important;",
                "maxlength": "22",
                "minlength": "8",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "required": "",
                "name": "password2",
                "id": "password2",
                "type": "password",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white",
                "placeholder": "Re-enter your password",
                "style": "height: 50px !important; margin-top: 20px !important;",
                "maxlength": "22",
                "minlength": "8",
            }
        )

    username = forms.CharField(max_length=30, label=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class LoginForm(AuthenticationForm):
    username =  forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "required": "",
                "name": "username",
                "id": "username",
                "type": "text",
                "class": "form-input w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "placeholder": "Username",
                "style": "height: 50px !important; margin-top: 20px !important;",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "required": "",
                "name": "password",
                "id": "password",
                "type": "password",
                "class": "w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5",
                "placeholder": "Password",
                "style": "height: 50px !important; margin-top: 20px !important;",
                "maxlength": "22",
                "minlength": "8",
            }
        )