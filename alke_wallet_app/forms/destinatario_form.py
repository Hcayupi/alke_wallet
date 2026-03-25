from django import forms

from alke_wallet_app.models.destinatarios import Destinatario


class DestinatarioForm (forms.ModelForm):

    wallet_codigo = forms.CharField(
        label = "ID Wallet",
        max_length=13,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
            }
        )
    )
    nombre = forms.CharField(
        label="Nombre",
        max_length=30,
        widget= forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    apellido = forms.CharField(
        label="Apellido",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        max_length= 50,
        widget= forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    apodo = forms.CharField(
        label="Apodo",
        max_length=30,
        widget=forms.TextInput(
            attrs= {
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Destinatario
        fields=[
            "wallet_codigo",
            "nombre",
            "apellido",
            "email",
            "apodo"
            ]

