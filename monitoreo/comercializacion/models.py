# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Indicador 22. Comercializacion de cacao (periodo de referencia ultimo ciclo de 12 meses)

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
        
class AquienVende(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
        
class DondeVende(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
        
class Comercializacion(models.Model):
    producto = models.ForeignKey(Productos, null=True, blank=True)
    autoconsumo = models.FloatField('Volumen auto-consumo', null=True, blank=True)
    venta = models.FloatField('Volumen venta', null=True, blank=True)
    precio = models.FloatField('Precio de venta por unidad', null=True, blank=True)
    aquien_vende = models.ManyToManyField(AquienVende, verbose_name="¿A quién vende?", null=True, blank=True)
    donde = models.ManyToManyField(DondeVende, verbose_name="¿Dónde lo vende?", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "22-Comercialización de cacao"
        
class Tecnica(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
        
class Familia(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre

class CapacitacionTecnica(models.Model):
    capacitacion = models.ForeignKey(Tecnica, null=True, blank=True)
    respuesta = models.ManyToManyField(Familia, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "23-Capacitaciones técnica recibidas"
        
class Social(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
        
class CapacitacionSocial(models.Model):
    capacitacion = models.ForeignKey(Social, null=True, blank=True)
    respuesta = models.ManyToManyField(Familia, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "24-Capacitaciones en tema social recibidas"    
