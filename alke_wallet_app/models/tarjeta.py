from django.db import models
from .cuenta_bancaria import CuentaBancaria

class Tarjeta(models.Model):

    TIPO_TARJETA = [
        ("credito", "Crédito"),
        ("debito", "Débito"),
        ("prepago", "Prepago")
    ]

    cuenta_bancaria = models.ForeignKey(CuentaBancaria,null=True, on_delete=models.SET_NULL, related_name="tarjetas")
    numero_tarjeta = models.CharField(max_length= 19,  null= False)
    tipo_tarjeta = models.CharField(max_length= 20,choices=TIPO_TARJETA, null= False)
    fecha_expiracion = models.DateField( null= False)
    marca = models.CharField(max_length=20, null= False, default="credito")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero_tarjeta}"
