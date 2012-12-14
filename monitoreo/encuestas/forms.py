# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from monitoreo.encuestas.models import *
from monitoreo.lugar.models import *
from django.utils.translation import ugettext_lazy as _

ANOS_CHOICES = (('', u'Año'), (2009,'2009'), (2010,'2010'),(2011,'2011'),(2012,'2012'),(2013,'2013'),(2014,'2014'))
CHOICE_OPCION_F = (('', u'Socio'),(1,'Si'),(2,'No'))
CHOICE_DESDE_F = (('','Desde'),(1,"Menos de 5 año"),(2,"Mas de 5 años"))
CHOICE_DUENO_F = (('', _(u'Sexo Dueño')),(1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),(5,"Colectivo"),(6,"No hay"))
CHOICE_SEXO = (('', _(u'Sexo beneficiario')),(1,'Hombre'),(2,'Mujer'))
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

def get_anios():
    years = []
    for en in Encuesta.objects.order_by('year').values_list('year', flat=True):
        years.append((en, en))
    return list(set(years))

class MonitoreoForm(forms.Form):
    fecha = forms.MultipleChoiceField(choices=get_anios())
    departamento = forms.ModelMultipleChoiceField(queryset=departamentos(), required=False, label=u'Departamentos')
    organizacion = forms.ModelMultipleChoiceField(queryset=OrganizacionOCB.objects.all().order_by('nombre'), required=False, label=u'Organización')
    municipio = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all().order_by('nombre'), required=False)
    comunidad = forms.ModelMultipleChoiceField(queryset=Comunidad.objects.all(), required=False)
    #grupo = forms.ChoiceField(label = 'Grupo Etnico', choices = CHOICE_ETNICO, required=False)
    grupo = forms.MultipleChoiceField(choices = CHOICE_ETNICO, required=False)
    sexo = forms.ChoiceField(choices = CHOICE_SEXO,label = _('Sexo beneficiario'), required=False)
    dueno = forms.ChoiceField(label = _('Dueño'), choices = CHOICE_DUENO_F , required=False, initial=u"Dueño")

class MapaForm(forms.Form):
    fecha1 = forms.ChoiceField(choices=get_anios(), label = _('fecha'))