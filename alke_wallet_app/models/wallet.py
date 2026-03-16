from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Wallet(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="wallet", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default= 0)
    divisa  = models.CharField(max_length=10, default="CLP")
    estado = models.CharField(max_length=20, default="activa") #suspendida, cerrada
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.balance} - {self.divisa}"
