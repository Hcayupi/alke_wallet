from django.db import models
from django.conf import settings


class CuentaBancaria(models.Model):

    TIPO_CUENTA=[
        ("vista", "Vista"),
        ("corriente", "Corriente"),
        ("chequera_electronica", "Chequera electrónica"),
        ("cuenta_rut", "Cuenta Rut")
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cuenta_bancaria")
    nombre_banco = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=30)
    tipo_cuenta = models.CharField(max_length=20, choices=TIPO_CUENTA)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.nombre_banco} - {self.numero_cuenta}"