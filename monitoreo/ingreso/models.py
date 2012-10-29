# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# Indicador 11-  Ingreso Familiar. Venta de rubros (periodo de referencia de mayo 2009 a abril 2010)

CHOICE_VENDIO = ((1, (u'Comunidad')),
                 (2, (u'Intermediario')),
                 (3, (u'Mercado')),
                 (4, (u'Cooperativa')),
                 (5, (u'Todos'))
                 )

CHOICE_VENDIO_EN = ((1, (u'Comunity')),
                    (2, (u'intermediary')),
                    (3, (u'Market')),
                    (4, (u'Cooperativa')),
                    (5, (u'All'))
                    )

CHOICE_MANEJA = ((1, (u'Hombre')),
                 (2, (u'Mujer')),
                 (3, (u'Ambos')),
                 (4, (u'Hijos/as')),
                 (5, (u'Hombre-Hijos')),
                 (6, (u'Mujer-Hijos')),
                 (7, (u'Todos'))
                 )

CHOICE_MANEJA_EN = ((1, (u'Men')),
                    (2, (u'Woman')),
                    (3, (u'Both')),
                    (4, (u'Children/s')),
                    (5, (u'Men-Son')),
                    (6, (u'Women-Son')),
                    (7, (u'All'))
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
