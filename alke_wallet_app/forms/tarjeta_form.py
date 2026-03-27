from django import forms

from alke_wallet_app.enum.marca_tarjeta_enum import MarcaTarjeta
from alke_wallet_app.enum.tipo_direccion_enum import TipoDireccion
from alke_wallet_app.models.cuenta_bancaria import CuentaBancaria
from alke_wallet_app.models.tarjeta import Tarjeta 

class TarjetaForm(forms.ModelForm):
    cuenta_bancaria = forms.ModelChoiceField(
        queryset=CuentaBancaria.objects.none(),
        label="Cuenta Bancaria",
        widget=forms.Select(
            attrs={
                "class":"form-control"
            }
        ),
        empty_label="Seleccione cuenta bancaria",
        required=True,
        error_messages={"required":"Debes asociar una cuenta bancaria"}
    )
    numero_tarjeta = forms.IntegerField(
        label="Número de tarjeta",
        widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "placeholder": "1234 5678 9012 3456"
            }
        )
    )
    tipo_tarjeta = forms.ChoiceField(
    label="Tipo de tarjeta",
    choices=TipoDireccion.choices,
    initial=TipoDireccion.CREDITO,
    widget= forms.Select(
            attrs={
                "class":"form-control"
            }
    )
    )

    fecha_expiracion = forms.DateField(
        label="Fecha de expiración",
        input_formats = ['%m/%y', '%m/%Y'],
        widget=forms.DateInput(
            attrs={
            "class":"form-control",
            'placeholder': 'MM/YY'
            }
        )
    )

    marca = forms.ChoiceField(
        label="Marca",
        choices = MarcaTarjeta.choices,
        initial= MarcaTarjeta.VISA,
         widget= forms.Select(
            attrs={
                "class":"form-control"
            }
    )
        
    )


    class Meta:
        model = Tarjeta
        fields = ["cuenta_bancaria","numero_tarjeta","tipo_tarjeta","fecha_expiracion", "marca"]

    
    
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop("usuario", None)
        super().__init__(*args, **kwargs)

        if usuario:
            self.fields["cuenta_bancaria"].queryset = CuentaBancaria.objects.filter(
                usuario = usuario
            )
