from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import CreateView, UpdateView
from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Autor
# Create your views here.


def vista_presentacion(request):
    return render(request, 'app_autores/presentacion.html')


def detalle_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    return render(request,
                  'app_autores/detalle.html',
                  {'autor': autor})


def listar_autores(request):
    autores = Autor.objects.all()
    return render(request,
                  'app_autores/listar.html',
                  {'autores': autores})


def listar_autores_activos(request):
    autores = Autor.objects.all().filter(activo=True)
    return render(request,
                  'app_autores/listar.html',
                  {'autores': autores})


def listar_autores_inactivos(request):
    autores = Autor.objects.all().filter(activo=False)
    return render(request,
                  'app_autores/listar.html',
                  {'autores': autores})


def listar_autores_json(request):
    autores = get_list_or_404(Autor)
    autores_json = serializers.serialize('json', autores)
    return JsonResponse(autores_json, safe=False)


def borrar_autor(request, id):
    autor_a_borrar = get_object_or_404(Autor, id=id)
    autor_a_borrar.delete()
    return HttpResponseRedirect(reverse('app_autores:lista_autores'))


def modificar_estado(request, id):
    autor_a_modificar = get_object_or_404(Autor, id=id)
    autor_a_modificar.activo = not autor_a_modificar.activo
    autor_a_modificar.save()
    return HttpResponseRedirect(reverse('app_autores:lista_autores'))


class AutorCreateView(CreateView):
    model = Autor
    fields = '__all__'
    success_url = reverse_lazy('app_autores:lista_autores')
    template_name = 'crear.html'


class AutorUpdateView(UpdateView):
    model = Autor
    fields = '__all__'
    success_url = reverse_lazy('app_autores:lista_autores')
    template_name = 'crear.html'
