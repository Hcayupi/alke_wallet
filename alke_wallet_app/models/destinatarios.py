from django.db import models
from django.conf import settings

from alke_wallet_app.models.wallet import Wallet


class Destinatario (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mis_destinatarios")
    wallet_codigo = models.CharField(max_length= 12, null=True, blank=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        if self.wallet_codigo:
            return f"{self.nombre} {self.apellido} - ID wallet : {self.wallet_codigo}"
        return f"{self.nombre} {self.apellido} - ID wallet : Sin wallet"
