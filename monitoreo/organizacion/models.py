# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.encuestas.models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# Indicador 2. Organizacion gremial

class OrgGremiales(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizaciones Gremiales"

class BeneficiosObtenido(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Benificios Obtenidos"

CHOICE_DESDE = ((1, _(u'Menos de 5 años')),
                (2, _(u'Más de 5 años')),
                (3,  _(u'No utilizar'))
                )
                
CHOICE_MIEMBRO_GREMIAL = ((1, _(u'Junta directiva')),
                          (2, _(u'No')),
                          (3, _(u'Comisiones de trabajo'))
                          )


class OrganizacionGremial(models.Model):
    ''' 2. Organizacion Gremial
    '''
    socio = models.ManyToManyField(OrgGremiales,
                                   verbose_name="Es socio/a de una organización gremial", null=True, blank=True)
    desde_socio = models.IntegerField('Desde cuando', choices=CHOICE_DESDE, null=True, blank=True)
    beneficio = models.ManyToManyField(BeneficiosObtenido,
                                       verbose_name="¿Qué beneficios ha tenido por ser socio/a de la cooperativa, la asociación o empresa", null=True, blank=True)
    miembro_gremial = models.IntegerField('Soy miembro de órgano gremial',
                                          choices=CHOICE_MIEMBRO_GREMIAL, null=True, blank=True)
    
    capacitacion = models.IntegerField('He recibido capacitación para desempeñar mi cargo',
                                      choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "2.1-Organizacion gremial"

# 2.1 Organización comunitaria

class OrgComunitarias(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizaciones comunitarias"

class BeneficioOrgComunitaria(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Beneficios de estar organizado en comunidad"

class NombreOrganizacion(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "¿Como se llaman estas organizaciones"

class OrganizacionComunitaria(models.Model):
    ''' 2.1 Organizacion comunitarias
    '''
    numero = models.IntegerField('¿Cuántas organizaciones están activas en la localidad o comunidad', null=True, blank=True)
    pertence = models.IntegerField('¿Pertenece a algunas organizaciones?', choices=CHOICE_OPCION, null=True, blank=True)
    cual_organizacion = models.ManyToManyField(OrgComunitarias, verbose_name="¿A cuál organización comunitaria pertenece?", null=True, blank=True)
    cual_beneficio = models.ManyToManyField(BeneficioOrgComunitaria, verbose_name="¿Cuáles son los beneficios de estar organizado", null=True, blank=True)
    cuantas = models.IntegerField('¿Cuántas organizaciones comunitarias han sido creadas o apoyadas por el proyecto', null=True, blank=True)
    organizaciones = models.ManyToManyField(NombreOrganizacion, verbose_name="¿Como se llaman estas organizaciones?", null=True, blank=True)
    pertence_org = models.IntegerField('¿Pertenece a algunas organizaciones?', choices=CHOICE_OPCION, null=True, blank=True)
    personas = models.IntegerField('¿Cuántas personas estan integradas en las organizaciones comunitarias apoyadas por el proyecto?', null=True, blank=True)
    involucradas = models.IntegerField('¿La organización comunitaria apoyada por el proyecto está involucrada en algún sub-proyecto?', choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "2.2-Organizacion comunitaria"
        
#-------------------------------------------------------------------------------
#Indicador 3 y 4 son demaciado pequeños para crear un app para ellos

CHOICE_TENENCIA = ((1, (u"Propia con escritura pública")),
                   (2, (u"Propia por herencia")),
                   (3, (u"Parcela en tierra comunitaria")),
                   (4, (u"Propias con promesa de venta")),
                   (5, (u"Propias con titulo de reforma agraria")),
                   (6, (u"Arrendada")),
                   (7, (u"Sin documento")),
                   (8, (u"Escritura posesoria"))
                   )

CHOICE_TENENCIA_EN = ((1, (u"Deed itself with")),
                   (2, (u"Own by inheritance")),
                   (3, (u"Plot for community land")),
                   (4, (u"Own with a promise of sale")),
                   (5, (u"Titled own land reform")),
                   (6, (u"leased")),
                   (7, (u"Not Document")),
                   (8, (u"writing possessory"))
                   )

                   
                   
CHOICE_DUENO = ((1, (u"Hombre")),
                (2, (u"Mujer")),
                (3, (u"Mancomunado")),
                (4, (u"Parientes")),
                (5, (u"Colectivo")),
                (6, (u"No hay"))
                )

CHOICE_DUENO_EN = ((1, (u"Men")),
                    (2, (u"Women")),
                    (3, (u"Shared")),
                    (4, (u"Kins")),
                    (5, (u"Collective")),
                    (6, (u"None"))
                )

class Tenencia(models.Model):
    ''' Modelo tipo de tenencia de la propiedad
    '''
    parcela = models.IntegerField('Tipo de tenencia Parcela', choices=CHOICE_TENENCIA, null=True, blank=True)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_parcela_display()
        
    class Meta:
        verbose_name_plural = "3 y 4 Tenencia y Documento legal"
