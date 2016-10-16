from django.db import models
from arboles.models import Arbol, Censista
from django.forms import ModelForm

class CensistaForm(ModelForm):
    class Meta:
        model = Censista
        fields = ['nombre', 'apellido', 'dni']


class ArbolForm(ModelForm):
    class Meta:
        model = Arbol
        fields = ['censista', 'nroFrente', 'especie', 'estadoSanitario', 'inclinacion','ahuecamiento',
        'altInterCables', 'altInterLuminarias', 'danosAMuros', 'danosAVeredas', 'cazuela', 'distanciaEntrePlantas',
        'distanciaAlMuro', 'podasAnteriores', 'circunferencia', 'observaciones', 'latitud', 'longitud', 'imagen']
