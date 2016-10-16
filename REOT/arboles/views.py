from django.shortcuts import render
from django.http import HttpResponse
from arboles.models import Arbol, Censista
from arboles.forms import CensistaForm, ArbolForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the arboles index.")

@csrf_exempt
def createArbol(request, nombre, apellido, dni):
    print('sep')
    print(request)
    if request.method == 'POST':
        try:
            censista = Censista.objects.get(dni=dni)
        except Censista.DoesNotExist:
            censista = Censista(nombre=nombre, apellido=apellido,dni=dni)
            censista.save()

        request.POST['censista'] = censista.id
        form = ArbolForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return  HttpResponse('Arbol creado')
        else:
            return HttpResponse(form.errors)
    else:
        return HttpResponse('Error al crear el arbol')

@csrf_exempt
def createCensita(request, nombre, apellido, dni):
    if request.method == 'POST':
        data = {'nombre': nombre,'apellido': apellido, 'dni': dni}
        form = CensistaForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse('Se creo el censista correctamente')
        else:
            return HttpResponse(form.errors)
    else:
        return HttpResponse('Error al crear el censista')
