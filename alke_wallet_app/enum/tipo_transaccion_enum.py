from django.db import models

class TipoTransaccion(models.TextChoices):
    COMPRA = "compra", "Compra"
    TRANSFERENCIA = "transferencia", "Transferencia"
    DEPOSITO = "deposito", "Depósito"
    RETIRO = "retiro", "Retiro"