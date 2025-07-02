from django.urls import path
from . import views

app_name = 'app_autores'

urlpatterns = [
    path('presentacion/', views.vista_presentacion, name='presentacion'),
    path('detalle/<int:id>/', views.detalle_autor, name='detalle'),
    path('lista_autores/', views.listar_autores, name='lista_autores'),
    path('lista_activos/', views.listar_autores_activos, name='lista_activos'),
    path('lista_inactivos/', views.listar_autores_inactivos, name='lista_inactivos'),
    path('lista_json/', views.listar_autores_json, name='lista_json'),
    path('borrar/<int:id>/', views.borrar_autor, name='borrar'),
    path('modificar_estado/<int:id>/',
         views.modificar_estado, name='modificar_estado'),
    path('crear/', views.AutorCreateView.as_view(), name='crear'),
    path('modificar/<int:pk>', views.AutorUpdateView.as_view(), name='modificar'),
]
