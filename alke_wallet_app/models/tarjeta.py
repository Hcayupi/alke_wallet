from django.db import models
from django.contrib.auth.models import User

class Tarjeta(models.Model):

    TIPO_TARJETA = [
        ("credito", "Crédito"),
        ("debito", "Débito"),
        ("prepago", "Prepago")
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(max_length= 20)
    tipo_tarjeta = models.CharField(max_length= 20,choices=TIPO_TARJETA)
    fecha_expiracion = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.first_name} - {self.tipo_tarjeta}"