# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Create your models here.

# Indicador 12 Otros ingresos.

class Fuentes(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otros-Ingreso - Fuentes"

class TipoTrabajo(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otro-Ingreso - TipoTrabajo"
      
class OtrosIngresos(models.Model):
    '''Otros ingresos
    '''
    fuente = models.ForeignKey(Fuentes)
    tipo = models.ForeignKey(TipoTrabajo, null=True, blank=True)
    meses = models.IntegerField('# Meses',null=True, blank=True)
    ingreso = models.IntegerField('Ingreso por mes',null=True, blank=True)
    tiene_ingreso = models.IntegerField(choices=CHOICE_MANEJA,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.fuente.nombre
    
    class Meta:
        verbose_name_plural = "12-Otros ingresos"
#-------------------------------------------------------------------------------
