import uuid
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.http import JsonResponse

from alke_wallet_app.forms.tarjeta_form import TarjetaForm

from ..services.historial_services import historial_transacciones_service
from ..services.historial_services import ingresos_gastos_service
from ..forms.contact_form import ContactoForm
from ..forms.user_form import SignUpForm
from ..forms.login_form import LoginForm
from ..models.wallet import Wallet

from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()
            login(request, user)
            
            return redirect("home")

        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    else:
        form = LoginForm(request)

    return render(request, "login/login.html", {"login_form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def signup_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        print("POST recibido")

        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            Wallet.objects.create(usuario = user, balance= 0)

            messages.success(request, "Usuario creado correctamente")

            return redirect("home")

    else:
        form = SignUpForm()

    return render(request, "registro/registro.html", {"signup_form": form})


def dashboard_view(request):
    return redirect("home")


@login_required
def home_view(request):
    
    if "form_data" in request.session:
        tarjeta_form = TarjetaForm(request.session["form_data"])
        tarjeta_form._errors = request.session["form_errors"]

        del request.session["form_data"]
        del request.session["form_errors"]
    else:
        tarjeta_form = TarjetaForm()

    wallet = request.user.wallet

    resumen = ingresos_gastos_service(request)
    
    total_ingresos = sum(resumen["ingresos"])
    total_egresos = sum(resumen["egresos"])

    context = {
        "tarjeta_form": tarjeta_form,
        "location": "Dashboard",
        "saldo": wallet.balance,
        "ingresos":total_ingresos,
        "egresos":total_egresos,
        "codigo_wallet": wallet.codigo
    }
    return render(request, "home/page.html", context)

@login_required
def historial_view(request):
    movimientos = historial_transacciones_service(request)

    context = {"location": "Movimientos", "movimientos":movimientos}
    return render(request, "historial/page.html", context)


@login_required
def contacto_view(request):

    if request.method == "POST":
        form = ContactoForm(request.POST)

        if form.is_valid():

            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            mensaje = form.cleaned_data["mensaje"]

            # Aquí iría guardar en BD o enviar correo

            messages.success(request, "Mensaje enviado correctamente ✅")
            return redirect("home")

        else:
            request.session["form_data"] = request.POST
            request.session["form_errors"] = form.errors
            return redirect("home")

    return redirect("home")

    """
    "request" es el objeto que reprenta la petición que se realiza
    desde el cliente (navegador)

    Trea información como:
    * request.method (GET / POST)
    * request.POST (datos enviados desde el formulario)
    * request.user
    """
    # 1) Si  el usuario envía el formulario (botón enviar/submit)
    # normalmente el navegador lo envía con método POST
    if request.method == "POST":  # Si es POST

        # 2) Creamos una instancia del formulario se rellena con los datos enviados
        # request.POST e sun diccionario con lo que llegó desde el <form>
        # ejemplo {"nombre": "", "email": "", "mensaje": ""}
        form = ContactoForm(request.POST)

        # 3) is_valid() ejecuta todas las validaciones del form
        # ejemplo:
        # - Campos requeridos
        # - Email invalido
        # - max_length, entre otros
        # Si algo falla, form.errors se llena con los mensajes de error y
        # form.is_valid() sería igual a False

        if form.is_valid():
            # 4) cleaned_data trae los datos ya validados y "limpios":
            # - strings con strip, conversiones de tipos de datos, etc.
            # - solo existe si is_valid() fue True

            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            mensaje = form.cleaned_data["mensaje"]

            # 5)Aquí realizariamos el procesamiento de la data o info:
            # -guardar en BD
            # -Enviar un correo
            # -crear un ticket, etc.

            # 6) Indicar al usuario que todo se proceso de manera correcta
            contex = {"nombre": nombre, "email": email, "mensaje": mensaje}
            return redirect("home")

        # 7) Si no es válido form.is_valid(), no entramos al return
        # y caemos en el render final de la función con:
        # - form con errores (form.errors)
        # - el template puede mostrar esos errores
        else:
            print(form.errors)

    else:
        request.session["form_data"] = request.POST
        request.session["form_errors"] = form.errors
        return redirect("home")

    return redirect("home")


def evolucion_api(request):
    data = ingresos_gastos_service(request)
    return JsonResponse(data)
