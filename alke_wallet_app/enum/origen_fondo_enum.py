from django.db import models

class OrigenFondo(models.TextChoices):
    PROPIO = "propio", "Propio"
    TERCERO = "tercero", "Tercero"