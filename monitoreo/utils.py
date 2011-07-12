# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
#from sisme.fed.models import Proyecto
#from sisme.contraparte.models import Informe
from django.utils import simplejson

def save_as_xls(request):
    tabla = request.POST['tabla']    
    response = render_to_response('xls.html', {'tabla': tabla, })
    response['Content-Disposition'] = 'attachment; filename=tabla.xls'
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Charset'] ='UTF-8'
    return response
