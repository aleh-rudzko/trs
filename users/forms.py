from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django import forms

class AuthenticationForm(BaseAuthenticationForm):
    error_messages = {
        'invalid_login': "Please enter a correct %(username)s and password. "
                       "Note that both fields may be case-sensitive.",
        'inactive': "This account is inactive.",
        'email_non_exist': "This e-mail doesn't belong to any account. Please make sure it's typed correctly",
        'wrong_password': "Password is incorrect. Please try again (it's case sensitive)"
    }
    def clean_username(self):
        if not get_user_model().objects.filter(email=self.cleaned_data.get('username')).exists():
            raise forms.ValidationError(
                self.error_messages['email_non_exist'],
                code='email_non_exist'
            )
        return self.cleaned_data.get('username')

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError(
                    self.error_messages['wrong_password'],
                    code='wrong_password'
                )
        return self.cleaned_data.get('password')