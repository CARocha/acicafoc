# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Create your models here.

# Indicador 6. Reforestación (periodo de referencia de mayo 2009 a abril 2010)

class Actividad(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actividades de reforestacion"

class Reforestacion(models.Model):
    ''' reforestacion
    '''
    reforestacion = models.ForeignKey(Actividad, verbose_name="Actividades de reforestación")
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.reforestacion.nombre
    
    class Meta:
        verbose_name_plural = "6-Reforestacion (periodo de referencia último ciclo de 12 meses)"

#-------------------------------------------------------------------------------
