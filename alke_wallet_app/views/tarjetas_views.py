from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect


from alke_wallet_app.forms.cuenta_bancaria_form import CuentaBancariaForm
from alke_wallet_app.forms.tarjeta_form import TarjetaForm
from ..models.tarjeta import Tarjeta
from django.contrib.auth.decorators import login_required

@login_required
def api_tarjetas(request):
    cuenta_id = request.GET.get("cuenta_id")
    tarjetas = Tarjeta.objects.filter(cuenta_bancaria_id = cuenta_id)
    data = [{
        "id": t.id,
         "numero_tarjeta": t.__str__(),
         "tipo_tarjeta": t.tipo_tarjeta} for t in tarjetas]
    return JsonResponse(data, safe = False)

def registrar_tarjeta(request):
    
    if request.method == "POST":

        tarjeta_form = TarjetaForm(request.POST, usuario=request.user)

        if tarjeta_form.is_valid():
            tarjeta_form.save()
          
            messages.success(request, "Tarjeta ingresada correctamente")
        else:
             
            request.session["form_data_tarjeta"] = request.POST
            request.session["form_errors_tarjeta"] = tarjeta_form.errors
            return redirect("home")

    return redirect("home")

def registrar_cuenta_bancaria(request):
    
    if request.method == "POST":

        CuentaBancaria_form = CuentaBancariaForm(request.POST)

        if CuentaBancaria_form.is_valid():

            CuentaBancaria_form = CuentaBancaria_form.save(commit=False)
            CuentaBancaria_form.usuario = request.user
            CuentaBancaria_form.save()
          
            messages.success(request, "Cuenta bancaria ingresada correctamente")
        else:
             
            request.session["form_data_cbanco"] = request.POST
            request.session["form_errors_cbanco"] = CuentaBancaria_form.errors
            return redirect("home")

    return redirect("home")
