from django import forms

from alke_wallet_app.enum.tipo_direccion_enum import TipoDireccion
from alke_wallet_app.models.tarjeta import Tarjeta 

class TarjetaForm(forms.ModelForm):
    cuenta_bancaria = forms.IntegerField(
        label="Número de cuenta",
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    tipo_tarjeta = forms.ChoiceField(
    label="Tipo de crédito",
    choices=TipoDireccion.choices,
    initial=TipoDireccion.CREDITO
    )
    fecha_expiracion = forms.CharField(
        label="Fecha de expiración",
        max_length=5,
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model = Tarjeta
        fields = ["cuenta_bancaria","tipo_tarjeta","fecha_expiracion"]