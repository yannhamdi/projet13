"""module that creates forms"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import User


class SignUpForm(UserCreationForm):
    """class for signup form"""
    class Meta:
        """class that gives details of the user information"""
        model = User
        fields = ('username', 'last_name', 'first_name',
                  'email', 'password1', 'password2')


class SignInForm(forms.Form):
    """class for signin form"""
    username = forms.CharField(label="username", max_length=20)
    password = forms.CharField(label="Mot-de-Passe",
                               widget=forms.PasswordInput,
                               min_length=6, max_length=16)

    def clean(self):
        """function that checks if user entry is correct"""
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Identifiants incorrects')
        return self.cleaned_data
