import uuid
from django.db import transaction
from alke_wallet_app.models.transaccion import Transaccion
from alke_wallet_app.models.wallet import Wallet
from alke_wallet_app.services.errores import SaldoInsuficienteError


def transferir(origen_id, destino_id, monto):
    with transaction.atomic():

        origen = Wallet.objects.select_for_update().get(id=origen_id)
        destino = Wallet.objects.select_for_update().get(id= destino_id)

        if origen.balance < monto:
            raise SaldoInsuficienteError("Saldo insuficiente")
        
        ref = uuid.uuid4()

        origen.saldo -= monto
        origen.save()

        destino.saldo += monto
        destino.save()

        Transaccion.objectts.create(
            wallet = origen,
            wallet_tercero = destino,
            tipo_transaccion = "transferencia",
            tipo_direccion = "debito",
            monto = monto,
            referencia = ref
        )

        Transaccion.objectts.create(
            wallet = destino,
            wallet_tercero = origen,
            tipo_transaccion = "transferencia",
            tipo_direccion = "crédito",
            monto = monto,
            referencia = ref
        )



