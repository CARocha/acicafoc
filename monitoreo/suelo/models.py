# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

# Create your models here.

# Indicador 10. Suelo

class Textura(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Textura"

class Profundidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Profundidad"

# Esta clase se va a ocupar en varias de los tipos de caraterización
# ya que contendra las opciones Alta, Media y Baja
class Densidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Densidad"

class Pendiente(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Pendiente"

class Drenaje(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Drenaje"

class Suelo(models.Model):
    ''' 12.1 - Caracterización de terreno
    '''
    textura = models.ManyToManyField(Textura,
                                     verbose_name="¿Cúal es el tipo de textura del suelo?", null=True, blank=True)
    profundidad = models.ManyToManyField(Profundidad,
                                         verbose_name="¿Cúal es la profundidad del suelo?", null=True, blank=True)
    lombrices = models.ManyToManyField(Densidad,
                                       verbose_name="¿Cómo es la presencia de lombrice en el suelo?",
                                       related_name="lombrices", null=True, blank=True)
    densidad = models.ManyToManyField(Densidad,
                                      verbose_name="¿Cómo es la densidad de raiz en la capa productiva de suelo?",
                                      related_name="densidad", null=True, blank=True)
    pendiente = models.ManyToManyField(Pendiente,
                                       verbose_name="¿Cúal es la pendiente del terrreno?", null=True, blank=True)
    drenaje = models.ManyToManyField(Drenaje,
                                     verbose_name="¿Cómo es el drenaje del suelo?", null=True, blank=True)
    materia = models.ManyToManyField(Densidad,
                                     verbose_name="Cómo en el contenido de materia orgánica",
                                     related_name="materia", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Suelo"

# 12.2 Manejo de suelo

class Preparar(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - preparar"

class Traccion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - tracción"

class Fertilizacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - fertilizacion"

class Conservacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - conservacion"

class ManejoSuelo(models.Model):
    ''' 12.2 Manejo de suelo
    '''
    preparan = models.ManyToManyField(Preparar, verbose_name="¿Cómo preparan sus terrenos?", null=True, blank=True)
    traccion = models.ManyToManyField(Traccion,
                                      verbose_name="¿Qué tipo de traccion utiliza para la preparación del suelo?", null=True, blank=True)
    analisis = models.IntegerField('¿Realiza análisis de fertilidad del suelo', choices=CHOICE_OPCION, null=True, blank=True)
    fertilizacion = models.ManyToManyField(Fertilizacion, verbose_name="¿Qué tipo de fertilización realiza?", null=True, blank=True)
    practica = models.IntegerField('¿Realiza práctica de conservación de suelo', choices=CHOICE_OPCION, null=True, blank=True)
    obra = models.ManyToManyField(Conservacion, verbose_name="¿Qué tipo de obra de conservación de suelo?", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Manejo de Suelo"

#-------------------------------------------------------------------------------
