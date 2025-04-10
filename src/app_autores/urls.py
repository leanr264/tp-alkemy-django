from django.urls import path
from . import views

app_name = 'app_autores'

urlpatterns = [
    path('presentacion/', views.vista_presentacion, name='presentacion')
]
