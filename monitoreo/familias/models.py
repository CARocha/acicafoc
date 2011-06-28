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
    total = models.IntegerField('Número total')
    no_leer = models.IntegerField('No sabe leer y escribir')
    p_incompleta = models.IntegerField('Primaria incompleta')
    p_completa = models.IntegerField('Primaria completa')
    s_incompleta = models.IntegerField('Secundaria incompleta')
    bachiller = models.IntegerField()
    universitario = models.IntegerField()
    f_comunidad = models.IntegerField('Viven fuera de la comunidad')
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
    pregunta = models.ForeignKey(PreguntaEnergia)
    respuesta = models.IntegerField(choices=CHOICE_OPCION)
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
    fuente = models.ManyToManyField(Fuente, verbose_name="Fuente de consumo de agua")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Agua"
#-------------------------------------------------------------------------------
