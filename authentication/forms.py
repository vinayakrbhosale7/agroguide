from django import forms
from django.contrib.auth.models import User
import re


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    # 🔹 Email validation (@gmail.com only)
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("Only Gmail addresses are allowed!")

        return email

    # 🔹 Password validation
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters!")

        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Must contain at least 1 uppercase letter!")

        if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
            raise forms.ValidationError("Must contain at least 1 special character!")

        return password