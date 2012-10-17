# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Create your models here.

# Indicador 15. cuales son los riesgos que hace la finca vulnerable

class Causa(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa"
        
class Fenomeno(models.Model):
    causa = models.ForeignKey(Causa)
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return '%s - %s' % (self.causa.nombre, self.nombre)
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa + fenomeno"
        
class Graves(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - daños graves"
        
class Vulnerable(models.Model):
    ''' 20 modelo vulnerable
    '''
    motivo = models.ForeignKey(Fenomeno)
    respuesta = models.ManyToManyField(Graves, verbose_name="¿Cada cuanto hay daños graves en la finca?", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "15- ¿Cuáles son los riesgos que hace la finca vulnerable?"
        
# Indicador 16. Mitigación de riesgos

class PreguntaRiesgo(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Riesgo - pregunta"

class Riesgos(models.Model):
    ''' 20 mitigacion de los riesgos
    '''
    pregunta = models.ForeignKey(PreguntaRiesgo, null=True, blank=True)
    respuesta = models.IntegerField('Respuesta', choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "16- Mitigación de los riesgos"
#-------------------------------------------------------------------------------
