from django import template

from alke_wallet_app.utils.utilities import formatear_monto

register = template.Library()

@register.filter
def clp(value):
  return formatear_monto(value)
    

