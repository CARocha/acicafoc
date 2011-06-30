# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Create your models here.

# Indicador 5 Uso de Tierrra

class Uso(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Uso de tierra"

class UsoTierra(models.Model):
    ''' Uso de tierra
    '''
    tierra = models.ForeignKey(Uso, verbose_name="Uso de Tierra", null=True, blank=True)
    area = models.FloatField('Área en Mz', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.tierra.nombre

#-------------------------------------------------------------------------------
