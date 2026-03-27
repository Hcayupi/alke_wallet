from django.db import models

class TipoDireccion(models.TextChoices):
    DEBITO = "debito", "Débito"
    CREDITO = "credito", "Crédito"
    PREPAGO = "prepago", "Prepago"