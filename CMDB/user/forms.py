from django import forms
import re

class RegisterForm(forms.Form) :
    name = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=64)
    password = forms.CharField(
        max_length=64,
        widget=forms.PasswordInput()
    )
    password_again = forms.CharField(
        max_length=64,
        widget=forms.PasswordInput()
    )

class LoginForm(forms.Form) :
    name = forms.CharField(max_length=32)
    password = forms.CharField(
        max_length=64,
        widget=forms.PasswordInput()
    )
