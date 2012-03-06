    # -*- coding: UTF-8 -*-
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from customfilefield import ContentTypeRestrictedFileField
from django.db import models
from django.template.defaultfilters import slugify
from south.modelsinspector import add_introspection_rules
from thumbs import ImageWithThumbsField
from utils import get_image_path, get_file_path
from django.utils.safestring import mark_safe



#from south.modelsinspector import add_introspection_rules
#add_introspection_rules = ([], ["^multimedia\.customfilefield\.ContentTypeRestrictedFileField"])



class CategoriaNoticia(models.Model):
    '''Modelo que representa la categorias de las noticias'''
    nombre = models.CharField('Título', max_length=250, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=40, unique=True, help_text='unico Valor', editable=False)

    def __unicode__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False):
        self.slug = slugify(self.nombre)
        super(CategoriaNoticia, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "Categoria de Actividad"
        verbose_name_plural = "Categorias de Actividad"


class Noticia(models.Model):
    '''Modelo que representa el tipo de contenido Noticias'''
    titulo = models.CharField('Título', max_length=120, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=120, unique=True, help_text='unico Valor', editable=False)
    fecha = models.DateField()
    categoria = models.ManyToManyField(CategoriaNoticia)
    contenido = models.TextField('Contenido', blank=True, null=True)
    #habilita_comentario = models.BooleanField(default=True)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Avances de proyecto"
        verbose_name_plural = "Avances de proyecto"
        ordering = ['-fecha']

    def save(self, force_insert=False, force_update=False):
        try:
            Noticia.objects.get(pk=self.id)
        except:
            n = Noticia.objects.all().count()
            self.slug = str(n) + '-' + slugify(self.titulo)
        super(Noticia, self).save(force_insert, force_update)

    #metodo para devolver la url exacta del objeto
    def get_full_url(self):
        return "/noticias/%s/" % self.slug

    #metodo para obtener el nombre del objeto
    def get_name(self):
        return self.titulo

#    def categorias(self):
#        return self.Noticia.all()[0].categoria.nombre

class NoticiaImagen(models.Model):
    '''fotos para las paginas'''
    titulo = models.CharField('Título', max_length = 100,blank = False, null = False)
    imagen = ImageWithThumbsField(upload_to=get_image_path, sizes=((218, 164), (640, 500)), help_text="Resolución minima 640x480")
    noticia = models.ForeignKey(Noticia)
    imgDir = 'attachments/imagenes/noticia'

    class Meta:
        verbose_name = "Avance proyecto imagen"
        verbose_name_plural = "Avance proyecto imagenes"

    def __unicode__(self):
        return str(self.image_img())

    def photo_name(self):
        return "Imagen %s" % self.pk

    def image_img(self):
        if self.imagen:
            return mark_safe('<img alt="%s" title="%s" width="80" height="52" src="%s" />' % (self.photo_name(), self.photo_name(), self.imagen.url_218x164))
        else:
            return '(Without image)'
    image_img.short_description = 'vista previa'
    image_img.allow_tags = True

class Adjunto(models.Model):
    nombre = models.CharField(max_length = 250)
#    adjunto = models.FileField(upload_to = 'attachments/documentos')
    adjunto = ContentTypeRestrictedFileField(upload_to = get_file_path, content_types=['application/pdf', 'application/zip','application/vnd.ms-powerpoint','application/vnd.ms-excel','application/msword','application/vnd.oasis.opendocument.text','application/vnd.oasis.opendocument.spreadsheet','application/vnd.oasis.opendocument.presentation'],max_upload_size=12582912, help_text='Solo se permiten archivos .doc .xls .ppt .docx .xlsx .pptx .pdf .zip .odp .odt .ods , tamaño máximo 12MB')
    noticia = models.ForeignKey(Noticia)
    fileDir = 'attachments/documentos'

#    def get_absolute_url(self):
#        return '%s%s/%s' % (settings.MEDIA_URL,
#                         settings.ATTACHMENT_FOLDER, self.id)
    def get_download_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.adjunto)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Adjunto"
        verbose_name_plural = "Adjuntos"

    def tipo(self):
        '''Devuelve la extension del archivo'''
        cadena = len(str(self.adjunto))
        tipo = str(self.adjunto)[cadena-3:cadena]
        return tipo
