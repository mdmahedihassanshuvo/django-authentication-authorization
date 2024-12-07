from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=15)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2') # noqa


class CustomLoginForm(forms.Form):
    identifier = forms.CharField(
        max_length=150,
        required=True,
        label="Username, Email, or Phone Number",
        widget=forms.TextInput(attrs={'placeholder': 'Username, Email, or Phone Number'})  # noqa
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        required=True
    )
