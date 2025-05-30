from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Frase

# Create your views here.


class FraseListView(ListView):
    model = Frase
    template_name = 'app_frases/listar.html'
    context_object_name = 'lista_frases'


class FrasesVisiblesListView(ListView):
    queryset = Frase.objects.all().filter(visible=True)
    template_name = 'app_frases/listar.html'
    context_object_name = 'lista_frases'


class FrasesNoVisiblesListView(ListView):
    queryset = Frase.objects.all().filter(visible=False)
    template_name = 'app_frases/listar.html'
    context_object_name = 'lista_frases'


class FraseCreateView(CreateView):
    model = Frase
    fields = '__all__'
    success_url = reverse_lazy('app_frases:lista_frases')
    template_name = 'crear.html'


class FraseUpdateView(UpdateView):
    model = Frase
    fields = '__all__'
    success_url = reverse_lazy('app_frases:lista_frases')
    template_name = 'crear.html'


class FraseDeleteView(DeleteView):
    model = Frase
    template_name = 'borrar.html'
    success_url = reverse_lazy('app_frases:lista_frases')
