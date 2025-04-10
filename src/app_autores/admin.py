from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_nacimiento', 'nacionalidad', 'activo']
    search_fields = ['nombre', 'nacionalidad']
