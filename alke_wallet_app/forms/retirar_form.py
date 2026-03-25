from django import forms
from ..models.transaccion import Transaccion

class RetiroForm(forms.ModelForm):
    monto = forms.IntegerField(
        label= "Monto a retirar",
        min_value= 1000,
        max_value= 5000000,
        widget=forms.NumberInput(
            attrs={
                "class":"form-control mb-3 mt-3",            
                "placeholder": "Monto a retirar",
            }
        )
    )

    observacion = forms.CharField(
        label = "Observación",
        max_length= 50,
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Observación",
                "style": "height:90px;",
                "rows":2
            }
        )
    )

    class Meta:
        model = Transaccion
        fields= [
            "monto", "observacion"
        ]
    
    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop("usuario", None)
        super().__init__(*args, **kwargs)

        
    def clean_monto(self):
        monto = self.cleaned_data.get("monto")

        if self.usuario and self.usuario.wallet.balance < monto:
            raise forms.ValidationError("Saldo insuficiente.")

        return monto