# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# Indicador 11-  Ingreso Familiar. Venta de rubros (periodo de referencia de mayo 2009 a abril 2010)

CHOICE_VENDIO = ((1, _(u'Comunidad')),
                 (2, _(u'Intermediario')),
                 (3, _(u'Mercado')),
                 (4, _(u'Cooperativa')),
                 (5, _(u'Todos'))
                 )

CHOICE_MANEJA = ((1, _(u'Hombre')),
                 (2, _(u'Mujer')),
                 (3, _(u'Ambos')),
                 (4, _(u'Hijos/as')),
                 (5, _(u'Hombre-Hijos')),
                 (6, _(u'Mujer-Hijos')),
                 (7, _(u'Todos'))
                 )
                 
CHOICE_CATEG = (
                 (1, _(u'Agroforestales')),
                 (2, _(u'Forestales')),
                 (3, _(u'Granos básicos')),
                 (4, _(u'Ganado mayor')),
                 (5, _(u'Animales de patio')),
                 (6, _(u'Hortalizas y frutas')),
                 (7, _(u'Musaceas')),
                 (8, _(u'Raíces y tubérculos'))
                     
                )

class Rubros(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    categoria = models.IntegerField(choices=CHOICE_CATEG, null = True, blank = True)
    nombre_en = models.CharField(max_length=50, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "IngresoFamiliar-Rubros"

class IngresoFamiliar(models.Model):
    ''' Modelo Ingreso familiar. venta de rubros
    '''
    rubro = models.ForeignKey(Rubros)
    cantidad = models.FloatField('Cantidad vendida en el año pasado',null=True, blank=True)
    consumida = models.FloatField('Cantidad consumida en el año pasado',null=True, blank=True)
    precio = models.FloatField('Precio de venta por unidad(C$ por unidad)',null=True, blank=True)
    quien_vendio = models.IntegerField('¿A quien vendio?', choices=CHOICE_VENDIO,null=True, blank=True)
    maneja_negocio = models.IntegerField('¿Quién maneja el negocio', choices=CHOICE_MANEJA,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.rubro.nombre
    
    class Meta:
        verbose_name_plural = "11- Ingreso familiar. Venta de rubros (período de referencia último ciclo de 12 meses)"

#-------------------------------------------------------------------------------
