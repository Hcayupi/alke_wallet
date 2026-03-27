import uuid
from django.db import transaction
from alke_wallet_app.enum.origen_fondo_enum import OrigenFondo
from alke_wallet_app.enum.tipo_direccion_enum import TipoDireccion
from alke_wallet_app.enum.tipo_transaccion_enum import TipoTransaccion
from alke_wallet_app.models.destinatarios import Destinatario
from alke_wallet_app.models.transaccion import Transaccion
from alke_wallet_app.models.wallet import Wallet
from alke_wallet_app.services.errores import SaldoInsuficienteError


def transferir(origen_id, destino_id, monto):
    with transaction.atomic():

        origen = Wallet.objects.select_for_update().get(id=origen_id)
        destino = Wallet.objects.select_for_update().get(id= destino_id)
        destinatario = Destinatario.objects.filter(wallet_codigo= destino.codigo).first()

        if origen.balance < monto:
            raise SaldoInsuficienteError("Saldo insuficiente")
        
        ref = uuid.uuid4()

        origen.balance -= monto
        origen.save()

        destino.balance += monto
        destino.save()

        Transaccion.objects.create(
            wallet = origen,
            wallet_tercero = destino,
            nombre_destinatario= destinatario.apodo,
            tipo_transaccion = TipoTransaccion.TRANSFERENCIA,
            tipo_direccion = TipoDireccion.DEBITO,
            origen_fondo = OrigenFondo.PROPIO,
            monto = monto,
            referencia = ref
        )

        Transaccion.objects.create(
            wallet = destino,
            wallet_tercero = origen,
            tipo_transaccion = TipoTransaccion.TRANSFERENCIA,
            tipo_direccion = TipoDireccion.CREDITO,
            origen_fondo = OrigenFondo.TERCERO,
            monto = monto,
            referencia = ref
        )



