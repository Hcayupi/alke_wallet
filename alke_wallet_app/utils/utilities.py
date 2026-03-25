def formatear_monto(value):
    try:
        if not value:
            return "$0"
        else:
            value = int(value)
            return "$" + "{:,}".format(value).replace(",", ".")
    except (ValueError, TypeError):
        return value

def parseMonth(value):
    MESES = [
        "", "Ene", "Feb", "Mar", "Abr", "May",
        "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
    ]
    return MESES[value]