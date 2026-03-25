from django import forms

from ..models import (Transaccion, Tarjeta, CuentaBancaria)


class DepositarForm(forms.ModelForm):
    monto =forms.IntegerField(
        label="Monto",
        min_value=20000,
        max_value=1000000,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Monto",
            }
        ),
        error_messages={
            "required": "El campo monto es obligatorio."
        },
    )
    entidad_bancaria = forms.ModelChoiceField(
        queryset=CuentaBancaria.objects.none(),
        label="Cuenta bancaria",
        widget=forms.Select(attrs={"class": "form-control", "id": "cuenta-select" }),
        empty_label="Seleccione una cuenta",
        required=True,
        error_messages={"required": "Debe seleccionar una cuenta bancaria."}
    )
    tarjeta_bancaria= forms.ModelChoiceField(
        queryset = Tarjeta.objects.none(),
        label="Tarjeta bancaria",
        widget=forms.Select(attrs={"class": "form-control", "id": "tarjeta-select"}),
        empty_label="Seleccione una tarjeta",
        required=True,
        error_messages={
             "required": "Debe seleccionar una tarjeta.",
        },
    )
    observacion= forms.CharField(
        label="Observación",
        max_length=50,
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Observación",
                "style": "height:90px;",
                "rows":2
            }
        ),
        error_messages={
            "max_length": "El nombre no puede superar los 50 caracteres.",
        },
    )

    class Meta:
        model= Transaccion
        fields = [
                "monto",
                "entidad_bancaria",
                "tarjeta_bancaria",
                "observacion"
            ]


    def clean_monto(self):

        monto = self.cleaned_data.get("monto")

        if monto < 20000:
            raise forms.ValidationError(
                "El monto mínimo para depositar es $20.000"
            )

        return monto
    
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop("usuario", None)
        super().__init__(*args, **kwargs)
        if usuario:
            self.fields["entidad_bancaria"].queryset = CuentaBancaria.objects.filter(usuario=usuario)
            self.fields["tarjeta_bancaria"].queryset = Tarjeta.objects.filter(cuenta_bancaria__usuario=usuario)