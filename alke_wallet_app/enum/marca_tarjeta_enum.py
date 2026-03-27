from django.db import models

class MarcaTarjeta(models.TextChoices):
    SELECCIONE = " ","Seleccione marca"
    MASTERCARD= "mastercard", "MasterCard"
    VISA = "visa", "Visa"
    TENPO = "tenpo", "Tenpo"