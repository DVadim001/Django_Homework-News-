from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    search = forms.CharField(max_length=256)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=128,
                             help_text='Введите правильный адрес')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
