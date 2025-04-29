from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Frase)
class FraseAdmin(admin.ModelAdmin):
    list_display = ['autor', 'frase', 'comentarios', 'fecha_frase', 'visible']
    search_fields = ['frase', 'fecha_frase']
