# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from monitoreo.encuestas.models import *
from monitoreo.lugar.models import *

ANOS_CHOICES = (('', u'Año'), (2009,'2009'), (2010,'2010'),(2011,'2011'),(2012,'2012'),(2013,'2013'),(2014,'2014'))
CHOICE_OPCION_F = (('', u'Socio'),(1,'Si'),(2,'No'))
CHOICE_DESDE_F = (('','Desde'),(1,"Menos de 5 año"),(2,"Mas de 5 años"))
CHOICE_DUENO_F = (('', u'Sexo Dueño'),(1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),(5,"Colectivo"),(6,"No hay"))
CHOICE_SEXO = (('', u'Sexo beneficiario'),(1,'Hombre'),(2,'Mujer'))
CHOICE_ETNICO = (
                    ('', u'Grupo Etnico'),
                    (1, 'Miskito'),
                    (2, 'Mayagna'),
                    (3, 'Mestizo'),
                    (4, 'Afrodescendiente')
              )

def departamentos():   
    foo = Encuesta.objects.all().order_by('comunidad__municipio__departamento__nombre').distinct().values_list('comunidad__municipio__departamento__id', flat=True)
    return Departamento.objects.filter(id__in=foo)

class MonitoreoForm(forms.Form):
    fecha = forms.MultipleChoiceField(choices=ANOS_CHOICES)
    departamento = forms.ModelMultipleChoiceField(queryset=departamentos(), required=False, label=u'Departamentos')
    organizacion = forms.ModelMultipleChoiceField(queryset=OrganizacionOCB.objects.all().order_by('nombre'), required=False, label=u'Organización')
    municipio = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all().order_by('nombre'), required=False)
    comunidad = forms.ModelMultipleChoiceField(queryset=Comunidad.objects.all(), required=False)
#    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
#            required=False, empty_label="Departamento")
#    organizacion = forms.CharField(widget = forms.Select, required=False)
#    municipio = forms.CharField(widget = forms.Select, required=False)
#    comunidad = forms.CharField(widget = forms.Select, required=False)
    grupo = forms.ChoiceField(label = 'Grupo Etnico', choices = CHOICE_ETNICO, required=False)
    sexo = forms.ChoiceField(choices = CHOICE_SEXO, required=False)
    dueno = forms.ChoiceField(label = 'Dueño', choices = CHOICE_DUENO_F , required=False, initial=u"Dueño")
