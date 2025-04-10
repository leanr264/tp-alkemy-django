from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)

    PAISES_CHOICES = [
        ("ARG", "Argentina"),
        ("BR", "Brasil"),
        ("URU", "Uruguay"),
        ("USA", "Estados Unidos"),
        ("MX", "Mexico"),
        ("FRA", "Francia"),
        ("ALE", "Alemania"),
        ("ESP", "España"),
        ("ING", "Inglaterra"),
    ]

    nacionalidad = models.CharField(choices=PAISES_CHOICES)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
