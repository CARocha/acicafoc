# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# Indicador 1: Familia

CHOICE_EDUCACION = ((1, _(u'Hombre mas de 18 años')),
                    (2, _(u'Mujeres mas de 18 años')),
                    (3, _(u'Hombre de 7 a 18 años')),
                    (4, _(u'Mujeres de 7 a 18 años')),
                    (5, _(u'Niños menos de 6 años')),
                    (6, _(u'Niñas menos de 6 años'))
                    )

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
        verbose_name_plural = "1.1-Composición y Educacion"
#-------------------------------------------------------------------------------

class PreguntaEnergia(models.Model):
    pregunta = models.CharField(max_length=200)
    pregunta_en = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.pregunta

    class Meta:
        verbose_name_plural = "Pregunta sobre energia"
        
class Energia(models.Model):
    ''' 1.2 energia
    '''
    pregunta = models.ForeignKey(PreguntaEnergia, null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "1.2-Energia"
        
class TipoCocina(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)
    
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
    nombre_en = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Fuentes de consumo de agua"

class Agua(models.Model):
    ''' 1.3 Agua de consumo
    '''
    fuente = models.ManyToManyField(Fuente, verbose_name="Fuente de consumo de agua", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "1.3-Agua de consumo"
#-------------------------------------------------------------------------------
