from django.shortcuts import render

# Create your views here.


def vista_presentacion(request):
    return render(request, 'base.html')
