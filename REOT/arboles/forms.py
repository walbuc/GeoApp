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
        fields = ['censista','calle', 'anchoVereda','vereda', 'nroFrente', 'nroArbol','especie', 'estadoSanitario', 'inclinacion','ahuecamiento',
        'altInterCables', 'altInterLuminarias', 'danosAMuros', 'danosAVeredas', 'cazuela','tipoDeTransito', 'distanciaEntrePlantas',
        'distanciaAlMuro', 'podasAnteriores', 'circunferencia', 'observaciones', 'latitud', 'longitud', 'imagen1','imagen2', 'imagen3','imagen4',
        'imagen5','imagen6','imagen7','imagen8','imagen9','imagen10']
