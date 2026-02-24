from django import forms
from django.contrib.auth.models import User as AuthUser


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label='Conferma Password',
    )

    class Meta:
        model = AuthUser
        fields = ['username', 'password']

def clean(self):
        cleaned_data = super().clean()  
        password = cleaned_data['password']
        password_confirm = cleaned_data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError('Le password non sono uguali!')

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput,
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
    )