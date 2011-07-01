# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *

class Vivero(models.Model):
    vivero_cacao = models.IntegerField('¿Actualmente tiene vivero de cacao en la finca?', choices=CHOICE_OPCION, null=True, blank=True)
    edad_planta = models.FloatField('Cúal es la edad de las plantas de vivero', null=True, blank=True)
    plantas = models.FloatField('¿Cuántas plantas hay en el vivero?', null=True, blank=True)
    planta_injerto = models.FloatField('¿Cuántas plantas son injertadas?', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return str(self.vivero_cacao)
        
    class Meta:
        verbose_name_plural = "Viveros"
        
class PlantaDesarrolloMenos(models.Model):
    cacao_desarrollo = models.IntegerField('¿Actualmente tiene plantas de cacao en desarrollo menos de un año?', choices=CHOICE_OPCION, null=True, blank=True)
    edad_planta = models.FloatField('Cúal es la edad de las plantas?', null=True, blank=True)
    area_sembrada = models.FloatField('¿Cuánta área está sembrada con cacao en desarrollo que tiene menos de un año?(Mz)', null=True, blank=True)
    plantas_finca = models.FloatField('¿Cuántas plantas de cacao en desarrollo menos de un año hay en la finca?', null=True, blank=True)
    planta_injerto = models.FloatField('¿Cuántas plantas de cacao en desarrollo menos de un año son injertadas?', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return str(self.cacao_desarrollo)
        
    class Meta:
        verbose_name_plural = "Plantas en desarrollo menos de un año"
        
class PlantaDesarrolloMas(models.Model):
    cacao_desarrollo = models.IntegerField('¿Actualmente tiene plantas de cacao en desarrollo más de un año?', choices=CHOICE_OPCION, null=True, blank=True)
    edad_planta = models.FloatField('Cúal es la edad de las plantas?', null=True, blank=True)
    area_sembrada = models.FloatField('¿Cuánta área está sembrada con cacao en desarrollo que tiene más de un año?(Mz)', null=True, blank=True)
    plantas_finca = models.FloatField('¿Cuántas plantas de cacao en desarrollo más de un año hay en la finca?', null=True, blank=True)
    planta_injerto = models.FloatField('¿Cuántas plantas de cacao en desarrollo más de un año son injertadas?', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return str(self.cacao_desarrollo)
        
    class Meta:
        verbose_name_plural = "Plantas en desarrollo más de un año"
        
class PlantaProduccion(models.Model):
    plantas_cacao = models.IntegerField('¿Actualmente tiene plantas de cacao en producción?', choices=CHOICE_OPCION, null=True, blank=True)
    edad_planta = models.FloatField('Cúal es la edad de las plantas (en años)', null=True, blank=True)
    area_sembrada = models.FloatField('¿Cuánta área está sembrada con cacao en producción?(Mz)', null=True, blank=True)
    plantas_finca = models.FloatField('¿Cuántas plantas de cacao en producción hay en la finca?', null=True, blank=True)
    planta_injerto = models.FloatField('¿Cuántas plantas de cacao en producción son injertadas?', null=True, blank=True)
    total = models.FloatField('¿Cuál es la producción total de cacao en la finca?(qq granos seco)', null=True, blank=True)
    sin_fermentar = models.FloatField('¿Cuál es la producción de cacao sin fermentar en la finca?(qq granos seco)', null=True, blank=True)
    fermentado = models.FloatField('¿Cuál es la producción de cacao fermentado  convencional en la finca?(qq granos seco', null=True, blank=True)
    organico = models.FloatField('¿Cuál es la producción de cacao fermentado orgánico en la finca?(qq granos seco', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
        
    def __unicode__(self):
        return str(self.plantas_cacao)

    class Meta:
        verbose_name_plural = "Plantas en producción"    
        
class PlantaElite(models.Model):    
    elite = models.IntegerField('¿Actualmente tiene plantas élites seleccionadas en la finca?',choices=CHOICE_OPCION, null=True, blank=True)
    edad_planta = models.FloatField('Cuál es la edad de las plantas élite?(en años)', null=True, blank=True)
    cuantas = models.FloatField('¿Cuántas plantas élites de cacao hay en la finca?', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return str(self.elite)

    class Meta:
        verbose_name_plural = "Plantas élite de cacao"
        
class Costo(models.Model):
    mantenimiento_area = models.FloatField('En total, ¿Cuánto gasta usted en año para el mantenimiento del área de cacao? (C$)', null=True, blank=True)
    mantenimiento_finca = models.FloatField('En total, ¿Cuánto gasta usted en año para el mantenimiento de la finca? (C$)', null=True, blank=True) 
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Costo de producción"

class Practicas(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class ViveroPractica(models.Model):
    practica = models.ForeignKey(Practicas, verbose_name="Prácticas", null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Vivero - Prácticas"

class PracticaEtapa(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
                
class PracticaFertilizacion(models.Model):
    practica = models.ForeignKey(PracticaEtapa, verbose_name="Prácticas", null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Etapa de producción y desarrollo: Prácticas de fertilización"
        
class PracticaFitosanitaria(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class PracticaManejoFitosanitario(models.Model):
    practica = models.ForeignKey(PracticaFitosanitaria, verbose_name="Prácticas", null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Etapa de producción y desarrollo: Prácticas de Manejo fitosanitario"

class PracticaProductivo(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class PracticaManejoProductivo(models.Model):
    practica = models.ForeignKey(PracticaProductivo, verbose_name="Prácticas", null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Etapa de producción y desarrollo: Prácticas de Manejo productivo"
        
class PracticaGenetico(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class PracticaMejoramientoGenetico(models.Model):
    practica = models.ForeignKey(PracticaGenetico, verbose_name="Prácticas", null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Etapa de producción y desarrollo: Prácticas de Mejoramiento genético de la plantación"
        
class PracticaPostcosecha(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
class PracticaManejoPostcosecha(models.Model):
    practica = models.ForeignKey(PracticaPostcosecha, verbose_name="Prácticas", null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Etapa de producción y desarrollo: Prácticas de Manejo postcosecha y beneficiado"

CHOICE_FERMENTACION = (
                        (1,"Menor de 80%"),
                        (2,"80%"),
                        (3,"Más de 80%")
                      )

CHOICE_SECADO = (
                        (1,"6%"),
                        (2,"6.5%"),
                        (3,"7%"),
                        (4,"Mayor de 7%")
                      )        
class Niveles(models.Model):
    nivel_fermentacion = models.IntegerField('Nivel de fermentación que maneja y aplica', choices=CHOICE_FERMENTACION, null=True, blank=True)
    nivel_secado = models.IntegerField('Nivel de humedad que maneja en el secado', choices=CHOICE_SECADO, null=True, blank=True)
    centro_acopio = models.IntegerField('¿Hay algún centro de acopio de cacao en la comunidad, comarca, zona o municipio al cual usted entregue su cacao?', choices=CHOICE_OPCION, null=True, blank=True)
    socio = models.IntegerField('¿Si usted es socio, asociado o miembro de algún centro de acopio de cacao', choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Preguntas 18,19,20,21"
