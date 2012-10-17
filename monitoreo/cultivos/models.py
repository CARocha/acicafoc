# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Indicador 8. Cultivos en la finca (periodo de referencia ultimo ciclo de 12 meses)

class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    nombre_en = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "CultivosFinca-Cultivos"

class CultivosFinca(models.Model):
    ''' indicador cultivos en la finca
    '''
    cultivos = models.ForeignKey(Cultivos)
    area =  models.FloatField('Área/Mz', null=True, blank=True)
    total = models.FloatField('Total producción por año', null=True, blank=True)
    consumo = models.FloatField('Consumo por año', null=True, blank=True)
    venta_libre = models.FloatField('Venta libre por año', null=True, blank=True)
    venta_organizada = models.FloatField('Venta organizada por año', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.cultivos.nombre
    
    class Meta:
        verbose_name_plural = "8-Cultivos en la finca"

#-------------------------------------------------------------------------------
