from django.db import models
from .transaccion import Transaccion



class Compra(models.Model):

    CATEGORIA=[
        ("alimentacion","Alimentación"),
        ("transporte", "Transporte"),
        ("servicio", "Servicio"),
        ("entretenimiento", "Entretenimiento")
    ]

    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE, related_name="compra")
    categoria = models.CharField(max_length=15,choices=CATEGORIA, null=False)
    comercio = models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
