# -*- coding: utf-8 -*-
from django.db import models
from monitoreo.lugar.models import *
from django.contrib.auth.models import User

class Recolector(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class OrganizacionOCB(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Organizaciones OCB"
        
class Etnico(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre

CHOICE_SEXO = (
                    (1, 'Hombre'),
                    (2, 'Mujer')
              )
              
CHOICE_OPCION = (
                    (1, 'Si'),
                    (2, 'No'),
                    (3,'No utilizar')
              )
              
CHOICE_ETNICO = (
                    (1, 'Miskito'),
                    (2, 'Mayagna'),
                    (3, 'Mestizo'),
                    (4, 'Afrodescendiente')
              )
              
CHOICE_MANEJA = ((1,"Hombre"),
                 (2,"Mujer"),
                 (3,"Ambos"),
                 (4,"Hijos/as"),
                 (5,'Hombre-Hijos'),
                 (6,'Mujer-Hijos'),
                 (7,'Todos'))

class Encuesta(models.Model):
    ''' Modelo de encuesta principal
    '''
    fecha = models.DateField()
    recolector = models.ForeignKey(Recolector, verbose_name="Nombre del Recolector")
    entrevistado = models.CharField('Nombre de Entrevistado/a', max_length=200)
    finca = models.CharField('Nombre de la finca', max_length=200, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, verbose_name="Nombre del Municipio")
    comunidad = models.ForeignKey(Comunidad, verbose_name="Nombre de la Comunidad")
    latitud = models.FloatField('Coordenada Latitud', blank=True, null=True)
    longitud = models.FloatField('Coordenada Longitud', blank=True, null=True)
#    latitud = models.DecimalField('Latitud', max_digits=8, decimal_places=5, blank=True, null=True)
#    longitud = models.DecimalField('Longitud', max_digits=8, decimal_places=5, blank=True, null=True) 
    sexo = models.IntegerField(choices=CHOICE_SEXO)
    beneficiario = models.ManyToManyField(OrganizacionOCB, verbose_name="Beneficiario/a de que OCB(organización comunitaria)", null=True, blank=True)
    grupo = models.IntegerField(choices=CHOICE_ETNICO, null=True, blank=True)
    usuario = models.ForeignKey(User)
    
    #campo oculto
    year = models.IntegerField(editable=True)
    
    def save(self):
        self.year = self.fecha.year
        super(Encuesta, self).save()
    
    def __unicode__(self):
        return self.entrevistado

    class Meta:
        verbose_name_plural = "Encuesta Linea base"
