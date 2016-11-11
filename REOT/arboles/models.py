from django.db import models

# Create your models here.

class Censista(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    def __str__(self):
        return self.nombre

class Arbol(models.Model):
    class Meta:
        verbose_name_plural = "Arboles"
    censista = models.ForeignKey(Censista, on_delete=models.CASCADE)
    calle = models.CharField(max_length=200, null=True)
    anchoVereda = models.FloatField(blank= True, null=True)
    vereda_opt = (
    ('NO', 'NO'),
    ('PAR', 'PAR'),
    ('IMPAR', 'IMPAR'),)
    vereda = models.CharField(choices=vereda_opt, max_length=3, null=True)
    nroFrente = models.IntegerField(blank=True, null=True)
    nroArbol = models.IntegerField()
    especie = models.CharField(max_length=200, blank=True, null=True)
    # S E D M
    estado_opt = (
    ('S', 'S'),
    ('D', 'D'),
    ('M','M'),)
    estadoSanitario = models.CharField(choices = estado_opt, max_length=1, blank=True, null=True)
    inclinacion_opt = (
    ('NO', 'NO'),
    ('LI', 'LI'),
    ('MI', 'MI'),)
    inclinacion = models.CharField(choices = inclinacion_opt, max_length=2, blank=True, null=True)
    ahuecamiento = models.CharField(max_length=10, blank=True, null=True)
    altInterCables_opt = (
    ('PD', 'PD'),
    ('PE', 'PE'),
    ('IA', 'IA'),)
    altInterCables = models.CharField(choices = altInterCables_opt, max_length=2, blank=True, null=True)
    altInterLuminarias_opt = (
    ('PD', 'PD'),
    ('PE', 'PE'),
    ('IA', 'IA'),)
    altInterLuminarias = models.CharField(choices =altInterLuminarias_opt, max_length=2, blank=True, null=True)
    danosAMuros_opt = (('SI', 'SI'),('NO', 'NO'),)
    danosAMuros = models.CharField(max_length=2, blank=True, choices = danosAMuros_opt, null=True)
    danosAVeredas_opt = (('NO', 'NO'),('L', 'L'),('I', 'I'))
    danosAVeredas = models.CharField(choices=danosAVeredas_opt, max_length=2, blank=True, null=True)
    cazuela_opt = (
    ('SI', 'SI'),
    ('NO', 'NO'),)
    #si o no
    cazuela = models.CharField(choices=cazuela_opt, max_length=2)
    tipo_de_transito_opt = (('PESADO', 'PESADO'),('PARTICULAR', 'PARTICULAR'),)
    tipoDeTransito = models.CharField(choices = tipo_de_transito_opt, max_length=10, blank=True, null=True)
    distanciaEntrePlantas = models.FloatField(blank=True, null=True)
    distanciaAlMuro = models.FloatField(blank=True, null=True)
    podas_opt = (
    ('NO', 'NO'),
    ('L', 'L'),
    ('S ', 'S'),)
    podasAnteriores = models.CharField(choices= podas_opt, max_length=2, blank=True, null=True)
    circunferencia = models.FloatField(blank=True, null=True)
    observaciones = models.CharField(max_length=400, blank=True, null=True)
    latitud = models.CharField('Latitud', max_length=200)
    longitud = models.CharField('Longitud', max_length=400)
    imagen1 = models.FileField(upload_to='uploads/')
    imagen2 = models.FileField(upload_to='uploads/', blank=True, null=True)
    imagen3 = models.FileField(upload_to='uploads/', blank=True, null=True)
    imagen4 = models.FileField(upload_to='uploads/', blank=True, null=True)
    imagen5 = models.FileField(upload_to='uploads/', blank=True, null=True)
    imagen6 = models.FileField(upload_to='uploads/', blank=True, null=True)
    imagen7 = models.FileField(upload_to='uploads/', blank=True, null=True)
    imagen8 = models.FileField(upload_to='uploads/', blank=True, null=True)
    imagen9 = models.FileField(upload_to='uploads/', blank=True, null=True)
    imagen10 = models.FileField(upload_to='uploads/', blank=True, null=True)
    pub_date = models.DateTimeField('fecha de publicacion', auto_now_add=True, null=True)

    def __str__(self):
        return self.especie
