from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from pacientes.models import Paciente

# Create your views here.
def bienvenida(request):
    return HttpResponse("Saludos")

def mostrar_edad(request, edad):
    calculo_edad = 20 + edad
    return HttpResponse(f'Tu edad despues de 20 años sera:{calculo_edad}')


def despedida(request):
    return HttpResponse ('<!DOCTYPE html>'
                         '<html><head></head><body><h1>Chao</h1></body>'
                         '</html>')


from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from pacientes.models import Paciente


# Create your views here.
def bienvenida(request):
    return HttpResponse ('Saludos')

def despedida(request):
    return HttpResponse ('<!DOCTYPE html>'
                         '<html><head></head><body><h1>Chao</h1></body>'
                         '</html>')

def bienvenida2(request):
    cantidad_pacientes = Paciente.objects.count()
    #pacientes = Paciente.objects.all()
    pacientes = Paciente.objects.order_by('apellido', 'nombre')
    #print(f'Cantidad personas: {cantidad_pacientes}')
    dict_datos = {'cantidad_pacientes':cantidad_pacientes, 'pacientes':pacientes}
    pagina = loader.get_template('bienvenido1.html')
    return HttpResponse(pagina.render(dict_datos, request))