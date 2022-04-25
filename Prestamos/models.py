from django.core.validators import RegexValidator
from django.db import models


class PedidoDePrestamos(models.Model):
    GENEROS = (
        ("Femenino", "Femenino"),
        ("Masculino", "Masculino")
    )

    validEmail = RegexValidator(
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        message="Ingrese un email válido")

    validString = RegexValidator(
        regex="[A-Za-z ]+$",
        message="Sólo caracteres alfabéticos y el del espacio, son permitidos")

    dni = models.IntegerField(blank=False, null=True)
    nombre = models.CharField(max_length=50, blank=False, null=True,
                              validators=[validString])
    apellido = models.CharField(max_length=50, blank=False, null=True,
                                validators=[validString])
    genero = models.CharField(max_length=9, choices=GENEROS,
                              default="Femenino", blank=False, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True,
                              validators=[validEmail])
    monto = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
