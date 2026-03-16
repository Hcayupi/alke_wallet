from django.db import models
from .wallet import Wallet

class Transaccion(models.Model):
    # El id se crea de manera automática
    TIPO_TRANSACCION=[
        #(Valor de BD, Valor de vista de Usuario)
        ("compra", "Compra"),
        ("transferencia", "Transferencia"),
        ("deposito", "Depósito"),
        ("retiro", "Retiro"),
    ]

    TIPO_DIRECCION=[
        ("debito", "Débito"),
        ("credito", "Crédito"),
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    tipo_transaccion = models.CharField(max_length=20, choices=TIPO_TRANSACCION)
    tipo_direccion = models.CharField(max_length=10, choices=TIPO_DIRECCION)
    cuenta_banco = models.ForeignKey("CuentaBancaria", on_delete=models.SET_NULL, null = True, blank =True)
    tarjeta = models.ForeignKey("Tarjeta", on_delete=models.SET_NULL, null= True, blank = True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transacción {self.tipo_transaccion} - {self.monto}"
