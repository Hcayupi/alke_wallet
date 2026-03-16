from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "idUser",
                "placeholder": "Usuario001",
            }
        ),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "idPass", "placeholder": "********"}
        ),
    )
