from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from alke_wallet_app.enum.tipo_direccion_enum import TipoDireccion
from alke_wallet_app.enum.tipo_transaccion_enum import TipoTransaccion

from alke_wallet_app.forms.destinatario_form import DestinatarioForm
from alke_wallet_app.models.wallet import Wallet
from alke_wallet_app.services.errores import SaldoInsuficienteError
from alke_wallet_app.services.transacciones_service import transferir
from alke_wallet_app.utils.utilities import formatear_monto
from ..forms.depositar_form import DepositarForm
from ..forms.retirar_form import RetiroForm
from ..forms.transferencia_form import TransferenciaForm 
from ..models.transaccion import Transaccion
from ..models.destinatarios import  Destinatario



def _actualizar_balance(wallet,operacion, monto):
      nuevo_balance = int(wallet.balance)

      if operacion == '+':
        nuevo_balance = nuevo_balance + int(monto)
      if operacion == '-':
        nuevo_balance = nuevo_balance - int(monto)

      wallet.balance = nuevo_balance
      wallet.save()
      wallet.refresh_from_db()



@login_required
def depositar_view(request):

    if request.method == "POST":
            form = DepositarForm(request.POST, usuario = request.user)

            if form.is_valid():
                wallet = request.user.wallet
                
                _actualizar_balance(wallet,'+', form.cleaned_data["monto"])

                Transaccion.objects.create(
                    wallet=wallet,
                    tipo_transaccion=TipoTransaccion.DEPOSITO,
                    tipo_direccion=TipoDireccion.CREDITO,
                    cuenta_banco=form.cleaned_data["entidad_bancaria"],
                    tarjeta=form.cleaned_data["tarjeta_bancaria"],
                    monto=form.cleaned_data["monto"],
                    descripcion=form.cleaned_data.get("descripcion", "")
                )

                return redirect("depositar")

    else:
        form = DepositarForm(usuario=request.user)

    return render(request, "fondos/depositar/page.html", {
         "depositar_form":form, 
         "location": "Depositar",
         })


@login_required
def retirar_view(request):

    if request.method == "POST":
        form = RetiroForm(request.POST, usuario = request.user)
        
        if form.is_valid():
            wallet = request.user.wallet
            
            _actualizar_balance(wallet,'-', form.cleaned_data["monto"])
            
            Transaccion.objects.create(
                    wallet=wallet,
                    tipo_transaccion=TipoTransaccion.RETIRO,
                    tipo_direccion=TipoDireccion.DEBITO,
                    monto=form.cleaned_data["monto"],
                    descripcion=form.cleaned_data.get("descripcion", "")
            )
    else:
        form = RetiroForm()
    balance = request.user.wallet.balance

    balance = formatear_monto(balance)
   
    context = {
         "location": "Retirar",
          "retirar_form":form, 
         "monto_actual":balance
        }
    return render(request, "fondos/retirar/page.html", context)


@login_required
def transferencias_view(request):

    if "form_data" in request.session:
        destinatario_form = DestinatarioForm(request.session["form_data"])
        destinatario_form._errors = request.session["form_errors"]

        del request.session["form_data"]
        del request.session["form_errors"]
    else:
        destinatario_form = DestinatarioForm()
     
    if request.method == "POST":
          transferencia_form = TransferenciaForm(request.POST, usuario = request.user)

          if transferencia_form.is_valid():
               origen = request.user.wallet
               destino = Wallet.objects.get(codigo=transferencia_form.cleaned_data["wallet_destino"])
               monto = int(transferencia_form.cleaned_data["monto"])
          
               try:
                    transferir(origen.id, destino.id, monto)

               except SaldoInsuficienteError as e:
                    messages.error(request, str(e))
    else:
        transferencia_form = TransferenciaForm(usuario = request.user)

    context = {
            "transferencia_form":transferencia_form, 
            "destinatario_form":destinatario_form, 
            "location": "Transferencia",
    }
     
    return render(request, "transferencias/page.html", context)


@login_required
def registro_destinatario(request):

    if request.method == "POST":
        destinatario_form = DestinatarioForm(request.POST)

        if destinatario_form.is_valid():

            nuevo_destinatario = destinatario_form.save(commit=False)
            nuevo_destinatario.usuario = request.user
            destinatario_form.save()
            
            messages.success(request, "Destinatario creado correctamente")

            return redirect("transferencia")

def api_codigo_wallet_destino(request):
     id_destinatario = request.GET.get("id_destinatario")
     destinatario = Destinatario.objects.filter(id=id_destinatario).first()

     data = {
        "cod_wallet": destinatario.wallet_codigo if destinatario else None
     }

     return JsonResponse(data)