from django.contrib import admin
from .models import Compra,Wallet, Transaccion,CuentaBancaria, Tarjeta

admin.site.register(Compra)
admin.site.register(CuentaBancaria)
admin.site.register(Tarjeta)
admin.site.register(Transaccion)
admin.site.register(Wallet)



