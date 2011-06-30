# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Create your models here.

# Indicador 1: Familia

CHOICE_EDUCACION = ((1,'Hombre mas de 18 años'),
                    (2,'Mujeres mas de 18 años'),
                    (3,'Hombre de 7 a 18 años'),
                    (4,'Mujeres de 7 a 18 años'),
                    (5,'Niños menos de 6 años'),
                    (6,'Niñas menos de 6 años'))

class Educacion(models.Model):
    ''' 1.1 - composicion y educacion
    '''
    sexo = models.IntegerField(choices=CHOICE_EDUCACION)
    total = models.IntegerField('Número total', null=True, blank=True)
    no_leer = models.IntegerField('No sabe leer y escribir', null=True, blank=True)
    p_incompleta = models.IntegerField('Primaria incompleta', null=True, blank=True)
    p_completa = models.IntegerField('Primaria completa', null=True, blank=True)
    s_incompleta = models.IntegerField('Secundaria incompleta', null=True, blank=True)
    bachiller = models.IntegerField(null=True, blank=True)
    universitario = models.IntegerField(null=True, blank=True)
    f_comunidad = models.IntegerField('Viven fuera de la comunidad', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_sexo_display()
        
    class Meta:
        verbose_name_plural = "Educacion"
#-------------------------------------------------------------------------------

class PreguntaEnergia(models.Model):
    pregunta = models.CharField(max_length=200)

    def __unicode__(self):
        return self.pregunta

    class Meta:
        verbose_name_plural = "Pregunta sobre energia"
        
class Energia(models.Model):
    ''' 1.3 energia
    '''
    pregunta = models.ForeignKey(PreguntaEnergia, null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Energia"
        
class TipoCocina(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Utiliza para cocinar"
        
class Cocina(models.Model):
    ''' Que utiliza para cocinar
    '''
    utiliza = models.ManyToManyField(TipoCocina, verbose_name="Qué utiliza para cocinar", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
#-------------------------------------------------------------------------------

class Fuente(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Fuentes de consumo de agua"

class Agua(models.Model):
    ''' 1.4 Agua de consumo
    '''
    fuente = models.ManyToManyField(Fuente, verbose_name="Fuente de consumo de agua", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Agua"
#-------------------------------------------------------------------------------
