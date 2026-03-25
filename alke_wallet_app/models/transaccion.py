from django.db import models
from django.core.exceptions import ValidationError
from .wallet import Wallet
import uuid

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

    ORIGEN_FONDO =[
        ("propio", "Propio"),
        ("tercero", "Tercero")
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transacciones")
    wallet_tercero = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, blank=True, related_name="transacciones_recibidas")
    nombre_destinatario = models.CharField(max_length=60, null=True, blank=True)
    tipo_transaccion = models.CharField(max_length=20, choices=TIPO_TRANSACCION)
    tipo_direccion = models.CharField(max_length=10, choices=TIPO_DIRECCION)
    origen_fondo = models.CharField(max_length=10, choices=ORIGEN_FONDO, default="propio", null=True)
    cuenta_banco = models.ForeignKey("CuentaBancaria", on_delete=models.SET_NULL, null = True, blank =True)
    tarjeta = models.ForeignKey("Tarjeta", on_delete=models.SET_NULL, null= True, blank = True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255, blank=True)
    referencia = models.UUIDField(default=uuid.uuid4, editable=False,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Transacción {self.tipo_transaccion} - {self.monto}"

    def clean(self):

        if self.tipo_transaccion == "transferencia":
            if not self.wallet_destino:
                raise ValidationError("Transferencia requiere ingresar wallet de destino")
            if self.wallet == self.wallet_destino:
                raise ValidationError("No puedes transferirte a ti mismo")
            
        if self.tipo_transaccion == "deposito" and self.tipo_direccion !="credito":
            raise ValidationError("Depósito debe ser tipo cŕedito")
        
        if self.tipo_transaccion == "retiro" and self.tipo_direccion !="debito":
            raise ValidationError("Retiro debe ser tipo debito")
        