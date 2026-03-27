from django.db.models.functions import Coalesce, ExtractMonth
from django.db.models import Sum, Case, When, IntegerField
from alke_wallet_app.enum.origen_fondo_enum import OrigenFondo
from alke_wallet_app.enum.tipo_direccion_enum import TipoDireccion
from alke_wallet_app.enum.tipo_transaccion_enum import TipoTransaccion
from alke_wallet_app.models.destinatarios import Destinatario
from alke_wallet_app.models.transaccion import Transaccion
from alke_wallet_app.utils.utilities import formatear_monto, parseMonth

def historial_transacciones_service(request):
    transacciones = Transaccion.objects.filter(wallet= request.user.wallet).order_by("-id")

    data = []
    for transaccion in transacciones:
        data.append({
            "codigo": transaccion.referencia,
            "fecha": transaccion.created_at,
            "descripcion": f"{transaccion.get_tipo_transaccion_display()} - {transaccion.wallet_tercero.usuario.username}" if transaccion.tipo_transaccion==TipoTransaccion.TRANSFERENCIA else f"{transaccion.get_tipo_transaccion_display()}" ,
            "cargos_giros": f"{formatear_monto(transaccion.monto)}" if transaccion.tipo_direccion == TipoDireccion.DEBITO else "$0",
            "abonos_depositos" : f"{formatear_monto(transaccion.monto)}" if transaccion.tipo_direccion == TipoDireccion.CREDITO else "$0"
            
            })
    return data

def historial_transferencias_service(request):
    transacciones = Transaccion.objects.filter(wallet= request.user.wallet,tipo_transaccion=TipoTransaccion.TRANSFERENCIA, origen_fondo=OrigenFondo.PROPIO ).order_by("-id")

    data = []
    for transaccion in transacciones:

        destinatario = Destinatario.objects.filter(wallet_codigo = transaccion.wallet_tercero.codigo).first()

        data.append({
            "codigo": transaccion.referencia,
            "fecha": transaccion.created_at,
            "destinatario": f"{destinatario.apodo}",
            "wallet_destino": f"{destinatario.wallet_codigo}",
            "monto" : f"{formatear_monto(transaccion.monto)}"
            
            })
    return data


def ingresos_gastos_service(request):
    transacciones = Transaccion.objects.filter(
        wallet=request.user.wallet
    ).annotate(
        mes=ExtractMonth("created_at")
    ).values("mes").annotate(
        ingresos=Coalesce(
            Sum(
                Case(
                    When(tipo_direccion=TipoDireccion.CREDITO, then="monto"),
                    default=0,
                    output_field=IntegerField()
                )
            ),
            0
        ),
        egresos=Coalesce(
            Sum(
                Case(
                    When(tipo_direccion=TipoDireccion.DEBITO, then="monto"),
                    default=0,
                    output_field=IntegerField()
                )
            ),
            0
        )
    ).order_by("mes")
    
    data = list(transacciones)

    labels = [parseMonth(label["mes"]) for label in data]
    ingresos = [ing["ingresos"] or 0 for ing in data]
    egresos = [egr["egresos"] or 0 for egr in data]

    return {"labels": labels, "ingresos": ingresos, "egresos": egresos}