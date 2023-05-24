from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    name = 'benjamin'

    # usuarios = Usuario.objects.all()

    return render(request, 'app/index.html', {'nombre': name})

def adios(request):
    return HttpResponse('adios')

def compras(request):
    return HttpResponse('asdasdasdasd')