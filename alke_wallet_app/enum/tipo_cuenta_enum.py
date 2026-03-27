from django.db import  models

class TipoCuenta(models.TextChoices):
    SELECCIONE = " ","Seleccione tipo cuenta"
    VISTA = "vista", "Vista"
    CORRIENTE = "corriente", "Corriente"
    CHEQUERA_ELETRONICA = "chequera_electronica", "Chequera electrónica"
    CUENTA_RUT = "cuenta_rut", "Cuenta Rut"