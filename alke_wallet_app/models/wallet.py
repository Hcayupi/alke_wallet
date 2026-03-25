from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid

def generar_codigo():
    return str(uuid.uuid4()).split("-")[4].upper()

class Wallet(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wallet")
    codigo = models.CharField(max_length=12, unique=True, default=generar_codigo)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default= 0)
    divisa  = models.CharField(max_length=10, default="CLP")
    estado = models.CharField(max_length=20, default="activa")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.balance} - {self.divisa}"
    

