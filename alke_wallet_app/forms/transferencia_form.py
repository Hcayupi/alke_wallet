from django import forms

from alke_wallet_app.models.destinatarios import Destinatario
from ..models.transaccion import Transaccion


class TransferenciaForm(forms.ModelForm):
        
        destinatario = forms.ModelChoiceField(
                    queryset = Destinatario.objects.none(),
                    label="Destinatario",
                    widget=forms.Select(attrs={"class": "form-control", "id": "destinatario-select"}),
                    empty_label="Seleccione un destinatario",
                    required=True,
                    error_messages={
                        "required": "Debe seleccionar un destinatario.",
                },
        )

        wallet_destino = forms.CharField(
                label = "Wallet destino",
                widget= forms.TextInput(
                        attrs={
                                "class":"form-control",                            
                        }
                ),
                required=True,
                error_messages={
                        "required": "Debe ingresar el ID Wallet del destinatario.",
                },
        )
        monto = forms.IntegerField(
                label= "Monto a transferir",
                min_value= 1000,
                max_value= 5000000,
                widget=forms.NumberInput(
                    attrs={
                        "class":"form-control mb-3 mt-3",                                  
                    }
                ),
                required=True,
                error_messages={
                        "required": "Debe ingresar el monto a transferir.",
                },
        )

        observacion = forms.CharField(
                label = "Observación",
                max_length= 50,
                required=False,
                widget=forms.Textarea(
                    attrs={
                        "class": "form-control",
                        "style": "height:90px;",
                        "rows":2
                    }
                )
        )

        class Meta:
            model = Transaccion
            fields = ["destinatario","wallet_destino", "monto", "observacion"]
        
        
        
        def __init__(self, *args, **kwargs):
            usuario = kwargs.pop("usuario", None)
            super().__init__(*args, **kwargs)

            if usuario:
                   self.fields["destinatario"].queryset = Destinatario.objects.filter(usuario=usuario)
                   self.fields["destinatario"].label_from_instance = lambda obj: f"{obj.nombre} {obj.apellido}"


