# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'CategoriaNoticia.nombre'
        db.alter_column('noticias_categorianoticia', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True))


    def backwards(self, orm):
        
        # Changing field 'CategoriaNoticia.nombre'
        db.alter_column('noticias_categorianoticia', 'nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250, null=True))


    models = {
        'noticias.adjunto': {
            'Meta': {'object_name': 'Adjunto'},
            'adjunto': ('monitoreo.noticias.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noticias.Noticia']"})
        },
        'noticias.categorianoticia': {
            'Meta': {'object_name': 'CategoriaNoticia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'})
        },
        'noticias.noticia': {
            'Meta': {'ordering': "['-fecha']", 'object_name': 'Noticia'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['noticias.CategoriaNoticia']", 'symmetrical': 'False'}),
            'contenido': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'noticias.noticiaimagen': {
            'Meta': {'object_name': 'NoticiaImagen'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('monitoreo.noticias.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noticias.Noticia']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['noticias']
