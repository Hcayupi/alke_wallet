from django import forms

from alke_wallet_app.enum.nombre_banco_enum import NombreBanco
from alke_wallet_app.enum.tipo_cuenta_enum import TipoCuenta
from alke_wallet_app.models.cuenta_bancaria import CuentaBancaria 

class CuentaBancariaForm (forms.ModelForm):
    nombre_banco = forms.ChoiceField(
        label="Nombre banco",
        choices=NombreBanco.choices,
        initial=NombreBanco.SELECCIONE,
        required = True,
        widget= forms.Select(
            attrs={
                "class":"form-control"
            }
        )
    )
    numero_cuenta = forms.IntegerField(
        label="Número cuenta",
        required = True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    tipo_cuenta = forms.ChoiceField(
        label="Tipo cuenta",
        choices=TipoCuenta.choices,
        initial=TipoCuenta.SELECCIONE,
        required = True,
        widget= forms.Select(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model = CuentaBancaria
        fields = ["nombre_banco", "numero_cuenta", "tipo_cuenta"]