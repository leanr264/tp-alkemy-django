from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Frase
from app_autores.models import Autor

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


def frases_por_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    frases = Frase.objects.filter(autor=autor)
    return render(request,
                  'app_frases/listar_por_autor.html',
                  {'autor': autor,
                   'frases': frases})


def listar_frases_visibles_json(request):
    frases = get_list_or_404(Frase.objects.all().filter(visible=True))
    frases_json = serializers.serialize('json', frases)
    return JsonResponse(frases_json, safe=False)
