# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Indicador 8. Cultivos en la finca (periodo de referencia ultimo ciclo de 12 meses)

class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "CultivosFinca-Cultivos"

class CultivosFinca(models.Model):
    ''' indicador cultivos en la finca
    '''
    cultivos = models.ForeignKey(Cultivos)
    area =  models.FloatField('Área/Mz')
    total = models.FloatField('Total producción por año')
    consumo = models.FloatField('Consumo por año')
    venta_libre = models.FloatField('Venta libre por año')
    venta_organizada = models.FloatField('Venta organizada por año')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.cultivos.nombre
    
    class Meta:
        verbose_name_plural = "Cultivos en la finca"

#-------------------------------------------------------------------------------
