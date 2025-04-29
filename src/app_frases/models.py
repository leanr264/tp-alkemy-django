from django.db import models
from app_autores.models import Autor

# Create your models here.


class Frase(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    frase = models.TextField()
    comentarios = models.CharField(max_length=100, null=True, blank=True)
    fecha_frase = models.DateField()
    visible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F'{self.frase}'

    class Meta:
        ordering = ['fecha_frase']
