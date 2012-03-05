# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CategoriaNoticia'
        db.create_table('noticias_categorianoticia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=40, db_index=True)),
        ))
        db.send_create_signal('noticias', ['CategoriaNoticia'])

        # Adding model 'Noticia'
        db.create_table('noticias_noticia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120, db_index=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('contenido', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('noticias', ['Noticia'])

        # Adding M2M table for field categoria on 'Noticia'
        db.create_table('noticias_noticia_categoria', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('noticia', models.ForeignKey(orm['noticias.noticia'], null=False)),
            ('categorianoticia', models.ForeignKey(orm['noticias.categorianoticia'], null=False))
        ))
        db.create_unique('noticias_noticia_categoria', ['noticia_id', 'categorianoticia_id'])

        # Adding model 'NoticiaImagen'
        db.create_table('noticias_noticiaimagen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('imagen', self.gf('monitoreo.noticias.thumbs.ImageWithThumbsField')(max_length=100)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['noticias.Noticia'])),
        ))
        db.send_create_signal('noticias', ['NoticiaImagen'])

        # Adding model 'Adjunto'
        db.create_table('noticias_adjunto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('adjunto', self.gf('monitoreo.noticias.customfilefield.ContentTypeRestrictedFileField')(max_length=100)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['noticias.Noticia'])),
        ))
        db.send_create_signal('noticias', ['Adjunto'])


    def backwards(self, orm):
        
        # Deleting model 'CategoriaNoticia'
        db.delete_table('noticias_categorianoticia')

        # Deleting model 'Noticia'
        db.delete_table('noticias_noticia')

        # Removing M2M table for field categoria on 'Noticia'
        db.delete_table('noticias_noticia_categoria')

        # Deleting model 'NoticiaImagen'
        db.delete_table('noticias_noticiaimagen')

        # Deleting model 'Adjunto'
        db.delete_table('noticias_adjunto')


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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
