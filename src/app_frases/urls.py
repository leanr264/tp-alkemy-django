from django.urls import path
from .views import (
    FraseListView,
    FrasesVisiblesListView,
    FrasesNoVisiblesListView,
    FraseCreateView,
    FraseUpdateView,
    FraseDeleteView,
    frases_por_autor,
    listar_frases_visibles_json,
)

app_name = 'app_frases'

urlpatterns = [
    path('lista_frases/', FraseListView.as_view(), name='lista_frases'),
    path('lista_visibles/', FrasesVisiblesListView.as_view(),
         name='lista_visibles'),
    path('lista_no_visibles/', FrasesNoVisiblesListView.as_view(),
         name='lista_no_visibles'),
    path('crear/', FraseCreateView.as_view(), name='crear'),
    path('modificar/<int:pk>/', FraseUpdateView.as_view(), name='modificar'),
    path('borrar/<int:pk>/', FraseDeleteView.as_view(), name='borrar'),
    path('lista_por_autor/<int:id>/', frases_por_autor, name='lista_por_autor'),
    path('visibles_json/', listar_frases_visibles_json, name='visibles_json'),
]
