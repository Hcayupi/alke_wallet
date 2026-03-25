from django.urls import path
from .views.wallet_views import (
    login_view,
    logout_view,
    signup_view,
    home_view,
    dashboard_view,
    historial_view,
    contacto_view,
    evolucion_api
)
from .views.transaccion_views import (
    retirar_view,
    depositar_view,
    transferencias_view,
    registro_destinatario,
    api_codigo_wallet_destino
)
from .views.tarjetas_views import(
    api_tarjetas
)

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("home/", home_view, name="home"),
    path("fondos/retirar/", retirar_view, name="retirar"),
    path("fondos/depositar/", depositar_view, name="depositar"),
    path("transferencias/", transferencias_view, name="transferencia"),
    path("destinatario/",registro_destinatario, name="destinatario"),
    path("historial/", historial_view, name="historial"),
    path("contacto/", contacto_view, name="contacto"),
    path("api/wallet/", api_codigo_wallet_destino, name="cod_wallet_api"),
    path("api/tarjetas/",api_tarjetas, name="tarjetas_api"),
    path("api/evolucion/", evolucion_api, name="evolucion_api"),
]
