from django.http import JsonResponse

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

        tarjeta_form = TarjetaForm(request.POST)

        if tarjeta_form.is_valid():
            tarjeta_form.save()
