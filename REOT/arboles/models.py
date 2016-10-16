from django.db import models

# Create your models here.

class Censista(models.Model):
    #id
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    def __str__(self):
        return self.nombre

class Arbol(models.Model):
    #id = models.IntegerField
    censista = models.ForeignKey(Censista, on_delete=models.CASCADE)
    nroFrente = models.IntegerField()
    especie = models.CharField(max_length=200)
    # S E D M
    estadoSanitario = models.CharField(max_length=1)
    inclinacion = models.FloatField()
    #porcentajes default null
    ahuecamiento = models.FloatField()
    altInterCables = models.CharField(max_length=2)
    altInterLuminarias = models.CharField(max_length=2)
    danosAMuros = models.CharField(max_length=2)
    danosAVeredas = models.CharField(max_length=2)
    cazuela = models.CharField(max_length=200)
    distanciaEntrePlantas = models.FloatField()
    distanciaAlMuro = models.FloatField()
    podasAnteriores = models.CharField(max_length=2)
    circunferencia = models.IntegerField()
    observaciones = models.CharField(max_length=400)
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=400)
    imagen = models.FileField(upload_to='uploads/')
    pub_date = models.DateTimeField('fecha de publicacion', auto_now_add=True)

    def __str__(self):
        return self.especie
