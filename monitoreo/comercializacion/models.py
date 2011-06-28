# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Indicador 22. Comercializacion de cacao (periodo de referencia ultimo ciclo de 12 meses)

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class AquienVende(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class DondeVende(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class Comercializacion(modes.Model):
    producto = models.ForeignKey(Productos)
    autoconsumo = models.FloatField('Volumen auto-consumo')
    venta = models.FloatField('Volumen venta')
    precio = models.FloatField('Precio de venta por unidad')
    aquien_vende = models.ManyToManyField(AquienVende, verbose_name="¿A quién vende?")
    donde = models.ManyToManyField(DondeVende, verbose_name="¿Dónde lo vende?")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Comercialización de cacao"
        
class Tecnica(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class Familia(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre

class CapacitacionTecnica(models.Model):
    capacitacion = models.ForeignKey(Tecnica)
    respuesta = models.ManyToManyField(Familia)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Capacitaciones técnicas recibidas"
        
class Social(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class CapacitacionSocial(models.Model):
    capacitacion = models.ForeignKey(Social)
    respuesta = models.ManyToManyField(Familia)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Capacitaciones en temas social recibidas"    
