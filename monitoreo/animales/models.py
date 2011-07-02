# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Indicador 7. Animales en la finca y la producción (periodo de referencia ciclo 12 meses)

class Animales(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Finca - Animales"

class ProductoAnimal(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Finca - Producto"


class AnimalesFinca(models.Model):
    ''' Modelo animales en la finca
    '''
    animales = models.ForeignKey(Animales)
    cantidad = models.FloatField(null=True, blank=True)
    produccion = models.ForeignKey(ProductoAnimal, null=True, blank=True)
    total_produccion = models.FloatField('Total producion por año', null=True, blank=True)
    consumo = models.FloatField('Consumo por año', null=True, blank=True)
    venta_libre = models.FloatField('Venta libre por año', null=True, blank=True)
    venta_organizada = models.FloatField('Venta organizada por año', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.animales.nombre
    
    class Meta:
        verbose_name_plural = "7-Animales en la finca y producción"
#-------------------------------------------------------------------------------
