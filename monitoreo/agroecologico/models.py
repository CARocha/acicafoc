# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# Indicador 9. Opciones de manejo agroecologico

class ManejoAgro(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    nombre_en = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Uso opciones de manejo agroecologico"

CHOICE_NIVEL_CONOCIMIENTO = ((1, _(u'Nada')),
                             (2, _(u'Poco')),
                             (3, _(u'Algo')),
                             (4, _(u'Bastante'))
                            )

class OpcionesManejo(models.Model):
    ''' opciones de manejo agroecologico
    '''
    uso = models.ForeignKey(ManejoAgro, verbose_name="Uso de opciones de manejo agroecologico", null=True, blank=True)
    nivel = models.IntegerField('Nivel de conocimiento', choices=CHOICE_NIVEL_CONOCIMIENTO, null=True, blank=True)
    menor_escala = models.IntegerField('Han experimentado en pequeña escala', choices=CHOICE_OPCION, null=True, blank=True)
    mayor_escala = models.IntegerField('Han experimentado en mayor escala', choices=CHOICE_OPCION, null=True, blank=True)
    volumen = models.FloatField('¿Qué área, número o volumen')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.uso.nombre
    
    class Meta:
        verbose_name_plural = "9-Opciones de manejo agroecologico"

#-------------------------------------------------------------------------------
