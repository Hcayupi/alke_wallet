from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese su nombre",
            }
        ),
        error_messages={
            "required": "El campo nombre es obligatorio.",
            "max_length": "El nombre no puede superar los 150 caracteres.",
        },
    )

    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese su correo electrónico",
            }
        ),
        error_messages={
            "required": "El correo es obligatorio.",
            "invalid": "Ingrese un correo válido.",
        },
    )

    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Escriba su mensaje aquí...",
            }
        ),
        error_messages={
            "required": "El mensaje no puede estar vacío.",
        },
    )

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]

        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError("El nombre no puede contener números.")

        return nombre
