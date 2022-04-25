from Prestamos.models import PedidoDePrestamos
from django import forms


class Formulario(forms.ModelForm):
    class Meta:
        model = PedidoDePrestamos

        fields = (
            "dni",
            "nombre",
            "apellido",
            "genero",
            "email",
            "monto"
        )

        labels = {
            "dni": "DNI",
            "nombre": "Nombre",
            "apellido": "Apellido",
            "genero": "Género",
            "email": "Email",
            "monto": "Monto"
        }

        validEmail = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        validString = r"[A-Za-z ]+"
        titleS = "Sólo caracteres alfabéticos y el del espacio, son permitidos"
        titleE = "Ingrese un email válido"

        widgets = {
            "dni": forms.NumberInput(attrs={"min": 0,
                                            "class": "form-control",
                                            "required": True}),
            "nombre": forms.TextInput(attrs={"class": "form-control",
                                             "pattern": validString,
                                             "title": titleS,
                                             "required": True}),
            "apellido": forms.TextInput(attrs={"class": "form-control",
                                               "pattern": validString,
                                               "title": titleS,
                                               "required": True}),
            "genero": forms.Select(attrs={"class": "form-select"}),
            "email": forms.EmailInput(attrs={"class": "form-control",
                                             "pattern": validEmail,
                                             "title": titleE,
                                             "required": True}),
            "monto": forms.NumberInput(attrs={"min": 0,
                                              "class": "form-control",
                                              "required": True})
        }
