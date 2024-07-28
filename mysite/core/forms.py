from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter username",
                "class": "py-4 px-6 rounded-xl",
                "style": "width: 100%",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                "class": "py-4 px-6 rounded-xl",
                "style": "width: 100%",
            }
        )
    )


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter username",
                "class": "py-4 px-6 rounded-xl",
                # TODO: fix w-full tailwind class not working
                "style": "width: 100%",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter Email",
                "class": "py-4 px-6 rounded-xl",
                "style": "width: 100%",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                "class": "py-4 px-6 rounded-xl",
                "style": "width: 100%",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "py-4 px-6 rounded-xl",
                "style": "width: 100%",
            }
        )
    )
