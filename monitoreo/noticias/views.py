# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.core.exceptions import ViewDoesNotExist

from noticias.models import *

def noticia_detalle(request,slug):
    '''Muestra el detalle de la noticia'''
    noticia = get_object_or_404(Noticia, slug=slug)
    #Jala las ultimas noticias relacionadas con la misma categoria y excluye a la noticia misma
    noticia_rel = Noticia.objects.filter(categoria=noticia.categoria).exclude(id = noticia.id).order_by('-fecha','-id')[:4]
    dicc = {'noticia': noticia,
            'noticia_rel':noticia_rel,
           }
    return direct_to_template(request, 'noticias/noticia_detalle.html',dicc)

def noticia_lista(request):
    '''Vista para mostrar la lista de noticia'''
    noticias = Noticia.objects.all().order_by('-fecha','-id')
    dicc = {'noticias': noticias,
           }
    return direct_to_template(request, 'noticias/noticia_lista.html',dicc)

def noticia_lista_tipo(request,tipo):
    '''Vista para mostrar la lista de noticia'''
    noticias = Noticia.objects.filter(tipo=tipo).order_by('-fecha','-id')
    dicc = {'noticias': noticias,'tipo':tipo,
           }
    return direct_to_template(request, 'noticias/noticia_lista.html',dicc)

def noticia_lista_cat(request,cat_slug):
    '''Filtra la lista de noticias por una categoria especifica'''
    noticias = Noticia.objects.filter(categoria__slug=cat_slug).order_by('-fecha','-id')
    categoria = CategoriaNoticia.objects.get(slug=cat_slug)

    dicc = {'noticias': noticias,'categoria':categoria,
           }
    return direct_to_template(request, 'noticias/noticia_lista.html',dicc)
