from django.urls import path
from .views import (
    login_view,
    logout_view,
    signup_view,
    home_view,
    dashboard_view,
    retirar_view,
    depositar_view,
    historial_view,
    contacto_view,
    evolucion_api,
    distribucion_api,
)

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("home/", home_view, name="home"),
    path("fondos/retirar/", retirar_view, name="retirar"),
    path("fondos/depositar/", depositar_view, name="depositar"),
    path("historial/", historial_view, name="historial"),
    path("contacto/", contacto_view, name="contacto"),
    path("api/evolucion/", evolucion_api, name="evolucion_api"),
    path("api/distribucion/", distribucion_api, name="distribucion_api"),
]
