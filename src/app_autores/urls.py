from django.urls import path
from . import views

app_name = 'app_autores'

urlpatterns = [
    path('presentacion/', views.vista_presentacion, name='presentacion'),
    path('detalle/<int:id>/', views.detalle_autor, name='detalle'),
    path('lista_activos/', views.listar_autores_activos, name='lista_activos'),
    path('lista_inactivos/', views.listar_autores_inactivos, name='lista_inactivos'),
    path('lista_json/', views.listar_autores_json, name='lista_json'),
]
