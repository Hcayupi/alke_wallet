from django.contrib import admin
from .models import Wallet, Transaccion,CuentaBancaria, Tarjeta, Destinatario

admin.site.register(CuentaBancaria)
admin.site.register(Tarjeta)
admin.site.register(Transaccion)
admin.site.register(Wallet)
admin.site.register(Destinatario)



