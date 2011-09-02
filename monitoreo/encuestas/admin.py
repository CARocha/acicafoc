# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User

from monitoreo.encuestas.models import *
from monitoreo.agroecologico.models import *
from monitoreo.animales.models import *
from monitoreo.bienes.models import *
from monitoreo.comercializacion.models import *
from monitoreo.cultivos.models import *
from monitoreo.estado.models import *
from monitoreo.familias.models import *
from monitoreo.genero.models import *
from monitoreo.ingreso.models import *
from monitoreo.lugar.models import *
from monitoreo.organizacion.models import *
from monitoreo.otrosIngresos.models import *
from monitoreo.reforestacion.models import *
from monitoreo.riesgos.models import *
from monitoreo.seguridad.models import *
from monitoreo.suelo.models import *
from monitoreo.tierra.models import *

#Familias
class EducacionInline(admin.TabularInline):
    model = Educacion
    extra = 1
    max_num = 6
    can_delete = False
    
class EnergiaInline(admin.TabularInline):
    model = Energia
    extra = 1
    max_num = 6
    can_delete = False
    
admin.site.register(PreguntaEnergia)

class CocinaInline(admin.TabularInline):
    model = Cocina
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(TipoCocina)

class AguaInline(admin.TabularInline):
    model = Agua
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(Fuente)

#Organizaciones
class OrganizacionGremialInline(admin.TabularInline):
    model = OrganizacionGremial
    fields = ['socio', 'desde_socio','beneficio', 'miembro_gremial', 
              'capacitacion']
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(OrgGremiales)
admin.site.register(BeneficiosObtenido)

class OrganizacionComunitariaInline(admin.TabularInline):
    model = OrganizacionComunitaria
    fields = ['numero', 'pertence', 'cual_organizacion', 
              'cual_beneficio','cuantas','organizaciones',
              'pertence_org','personas','involucradas']
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(OrgComunitarias)
admin.site.register(BeneficioOrgComunitaria)
admin.site.register(NombreOrganizacion)

class TenenciaInline(admin.TabularInline):
    model = Tenencia
    extra = 1
    max_num = 1
    can_delete = False
    
#Uso de tierra
class UsoTierraInline(admin.TabularInline):
    model = UsoTierra
    extra = 1
    max_num = 8
    #can_delete = False
    
admin.site.register(Uso)

#Reforestacion
class ReforestacionInline(admin.TabularInline):
    model = Reforestacion
    extra = 1
    can_delete = False
    
admin.site.register(Actividad)

#Animales
class AnimalesFincaInline(admin.TabularInline):
    model = AnimalesFinca
    extra = 1
    can_delete = False
    
admin.site.register(Animales)
admin.site.register(ProductoAnimal)

#cultivos
class CultivosFincaInline(admin.TabularInline):
    model = CultivosFinca
    extra = 1
    can_delete = False
    
admin.site.register(Cultivos)

#opciones de manejo agroecologico
class OpcionesManejoInline(admin.TabularInline):
    model= OpcionesManejo
    extra = 1
    can_delete = False
    
admin.site.register(ManejoAgro)

#Suelo
class SueloInline(admin.TabularInline):
    model = Suelo
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(Textura)
admin.site.register(Profundidad)
admin.site.register(Densidad)
admin.site.register(Pendiente)
admin.site.register(Drenaje)

class ManejoSueloInline(admin.TabularInline):
    model = ManejoSuelo
    fields = ['preparan','traccion','analisis','fertilizacion',
              'practica','obra']
    extra = 1
    max_num = 1
    can_delete = False

admin.site.register(Preparar)
admin.site.register(Traccion)
admin.site.register(Fertilizacion)
admin.site.register(Conservacion)

#Ingreso familiar
class IngresoFamiliarInline(admin.TabularInline):
    model = IngresoFamiliar
    fields = ['rubro','consumida','cantidad','precio',
              'quien_vendio','maneja_negocio']
    extra = 1
    can_delete = False

admin.site.register(Rubros)

#Otros ingresos
class OtrosIngresosInline(admin.TabularInline):
    model = OtrosIngresos
    extra = 1
    can_delete = False
    
admin.site.register(Fuentes)
admin.site.register(TipoTrabajo)

#Propiedades y bienes
class TipoCasaInline(admin.TabularInline):
    model = TipoCasa
    extra = 1
    max_num = 1
    can_delete = False
    
class DetalleCasaInline(admin.TabularInline):
    model = DetalleCasa
    extra = 1
    max_num = 1
    can_delete = False
    
class PropiedadesInline(admin.TabularInline):
    model = Propiedades
    extra = 1
    can_delete = False
    
class InfraestructuraInline(admin.TabularInline):
    model = Infraestructura
    extra = 1
    can_delete = False
    
class HerramientasInline(admin.TabularInline):
    model = Herramientas
    extra = 1
    can_delete = False
    
class TransporteInline(admin.TabularInline):
    model = Transporte
    extra = 1
    can_delete = False
   
admin.site.register(Casa)
admin.site.register(Piso)
admin.site.register(Techo)
admin.site.register(Equipos)
admin.site.register(Infraestructuras)
admin.site.register(NombreHerramienta)
admin.site.register(NombreTransporte)

#Seguridad alimentaria
class SeguridadInline(admin.TabularInline):
    model = Seguridad
    extra = 1
    can_delete = False
    
admin.site.register(Alimentos)

#Riesgos que hacen vulnerables las fincas
class VulnerableInline(admin.TabularInline):
    model = Vulnerable
    extra = 1
    can_delete = False

class RiesgosInline(admin.TabularInline):
    model = Riesgos
    extra = 1
    can_delete = False
    
admin.site.register(Causa)
admin.site.register(Fenomeno)
admin.site.register(Graves)
admin.site.register(PreguntaRiesgo)

#Estado actual
class ViveroInline(admin.TabularInline):
    model = Vivero
    extra = 1
    max_num = 1
    can_delete = False
    
class PlantaDesarrolloMenosInline(admin.TabularInline):
    model = PlantaDesarrolloMenos
    extra = 1
    max_num = 1
    can_delete = False
    
class PlantaDesarrolloMasInline(admin.TabularInline):
    model = PlantaDesarrolloMas
    extra = 1
    max_num = 1
    can_delete = False
    
class PlantaProduccionInline(admin.TabularInline):
    model = PlantaProduccion
    extra = 1
    max_num = 1
    can_delete = False
    
class PlantaEliteInline(admin.TabularInline):
    model = PlantaElite
    extra = 1
    max_num = 1
    can_delete = False
    
class CostoInline(admin.TabularInline):
    model = Costo
    extra = 1
    max_num = 1
    can_delete = False
    
admin.site.register(Practicas)

class ViveroPracticaInline(admin.TabularInline):
    model = ViveroPractica
    extra = 1
    can_delete = False
    
admin.site.register(PracticaEtapa)

class PracticaFertilizacionInline(admin.TabularInline):
    model = PracticaFertilizacion
    extra = 1
    can_delete = False
    
admin.site.register(PracticaFitosanitaria)

class PracticaManejoFitosanitarioInline(admin.TabularInline):
    model = PracticaManejoFitosanitario
    extra = 1
    can_delete = False
    
admin.site.register(PracticaProductivo)

class PracticaManejoProductivoInline(admin.TabularInline):
    model = PracticaManejoProductivo
    extra = 1
    can_delete = False
    
admin.site.register(PracticaGenetico)

class PracticaMejoramientoGeneticoInline(admin.TabularInline):
    model = PracticaMejoramientoGenetico
    extra = 1
    can_delete = False
    
admin.site.register(PracticaPostcosecha)

class PracticaManejoPostcosechaInline(admin.TabularInline):
    model = PracticaManejoPostcosecha
    extra = 1
    can_delete = False
    
class NivelesInline(admin.TabularInline):
    model = Niveles
    extra = 1
    max_num = 1
    can_delete = False
    
#comercializacion
class ComercializacionInline(admin.TabularInline):
    model = Comercializacion
    extra = 1
    can_delete = False
    
admin.site.register(Productos)
admin.site.register(AquienVende)
admin.site.register(DondeVende)
admin.site.register(Tecnica)
admin.site.register(Familia)

class CapacitacionTecnicaInline(admin.TabularInline):
    model = CapacitacionTecnica
    extra = 1
    can_delete = False
    
class CapacitacionSocialInline(admin.TabularInline):
    model = CapacitacionSocial
    extra = 1
    can_delete = False
    
admin.site.register(Social)

#Genero
class ParticipacionInline(admin.TabularInline):
    model = Participacion
    fields = ['principal','actividad_finca','ingreso','decision','proporcion']
    extra = 1
    max_num = 1
    #can_delete = False
    
class MujerOrganizacionInline(admin.TabularInline):
    model = MujerOrganizacion
    extra = 1
    max_num = 1
    #can_delete = False
    
admin.site.register(TipoOrganizacion)
admin.site.register(ActividadFinca)
admin.site.register(ActividadHogar)
#-------------------------------------------------------------------------------

class EncuestaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
        
    def queryset(self, request):
        qs = super(EncuestaAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)
        
    save_on_top = True
    actions_on_top = True
    exclude = ('usuario',)
    inlines = [EducacionInline,EnergiaInline,CocinaInline,AguaInline, 
               OrganizacionGremialInline,OrganizacionComunitariaInline,
               TenenciaInline,UsoTierraInline,ReforestacionInline, 
               AnimalesFincaInline,CultivosFincaInline,OpcionesManejoInline, 
               SueloInline,ManejoSueloInline,IngresoFamiliarInline, 
               OtrosIngresosInline,TipoCasaInline,DetalleCasaInline, 
               PropiedadesInline,InfraestructuraInline,
               HerramientasInline,TransporteInline, 
               SeguridadInline,VulnerableInline,RiesgosInline,ViveroInline,
               PlantaDesarrolloMenosInline,PlantaDesarrolloMasInline,
               PlantaProduccionInline,PlantaEliteInline,CostoInline,
               ViveroPracticaInline,PracticaFertilizacionInline,
               PracticaManejoFitosanitarioInline,PracticaManejoProductivoInline,
               PracticaMejoramientoGeneticoInline,PracticaManejoPostcosechaInline,
               NivelesInline,ComercializacionInline,CapacitacionTecnicaInline,
               CapacitacionSocialInline,ParticipacionInline,MujerOrganizacionInline
              ]
    list_display = ('entrevistado',)
    list_filter = ['municipio']
    search_fields = ['entrevistado']
    date_hierarchy = 'fecha'
               
admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Recolector)
admin.site.register(OrganizacionOCB)
admin.site.register(Etnico)
#-------------------------------------------------------------------------------
