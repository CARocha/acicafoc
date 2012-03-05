from django.contrib import admin
from monitoreo.noticias.models import Noticia, CategoriaNoticia, NoticiaImagen, Adjunto
from django.contrib.contenttypes import generic

class CategoriaNoticiaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    list_per_page = 12

class ImagenInline(admin.TabularInline):
    model = NoticiaImagen
    extra = 1
    max_num = 20
    template = "tabular.html"

class AdjuntoInline(admin.TabularInline):
    model = Adjunto
    extra = 1
    max_num = 3

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha']
    list_filter = ['categoria']
    search_fields = ['titulo']
    inlines = [AdjuntoInline,ImagenInline]
    save_on_top = True
    date_hierarchy = 'fecha'
    list_per_page = 12
    filter_horizontal =('categoria',)

    class Media:
        js = ['../files/js/tiny_mce/tiny_mce.js',
              '../files/js/editores/textareas.js',]


admin.site.register(CategoriaNoticia, CategoriaNoticiaAdmin)
admin.site.register(Noticia, NoticiaAdmin)

