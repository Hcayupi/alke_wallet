from django.db import models
from django.contrib.auth.models import User

class CuentaBancaria(models.Model):

    TIPO_CUENTA=[
        ("vista", "Vista"),
        ("corriente", "Corriente"),
        ("chequera_electronica", "Chequera electrónica"),
        ("cuenta_rut", "Cuenta Rut")
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_banco = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=30)
    tipo_cuenta = models.CharField(max_length=20, choices=TIPO_CUENTA)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str___(self):
        return f" {self.usuario.first_name} {self.usuario.first_name}: {self.nombre_banco} {self.tipo_cuenta}"