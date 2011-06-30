# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Casa'
        db.create_table('bienes_casa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bienes', ['Casa'])

        # Adding model 'Piso'
        db.create_table('bienes_piso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bienes', ['Piso'])

        # Adding model 'Techo'
        db.create_table('bienes_techo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bienes', ['Techo'])

        # Adding model 'TipoCasa'
        db.create_table('bienes_tipocasa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('bienes', ['TipoCasa'])

        # Adding M2M table for field tipo on 'TipoCasa'
        db.create_table('bienes_tipocasa_tipo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipocasa', models.ForeignKey(orm['bienes.tipocasa'], null=False)),
            ('casa', models.ForeignKey(orm['bienes.casa'], null=False))
        ))
        db.create_unique('bienes_tipocasa_tipo', ['tipocasa_id', 'casa_id'])

        # Adding M2M table for field piso on 'TipoCasa'
        db.create_table('bienes_tipocasa_piso', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipocasa', models.ForeignKey(orm['bienes.tipocasa'], null=False)),
            ('piso', models.ForeignKey(orm['bienes.piso'], null=False))
        ))
        db.create_unique('bienes_tipocasa_piso', ['tipocasa_id', 'piso_id'])

        # Adding M2M table for field techo on 'TipoCasa'
        db.create_table('bienes_tipocasa_techo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipocasa', models.ForeignKey(orm['bienes.tipocasa'], null=False)),
            ('techo', models.ForeignKey(orm['bienes.techo'], null=False))
        ))
        db.create_unique('bienes_tipocasa_techo', ['tipocasa_id', 'techo_id'])

        # Adding model 'DetalleCasa'
        db.create_table('bienes_detallecasa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tamano', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ambientes', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('letrina', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('bienes', ['DetalleCasa'])

        # Adding model 'Equipos'
        db.create_table('bienes_equipos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bienes', ['Equipos'])

        # Adding model 'Infraestructuras'
        db.create_table('bienes_infraestructuras', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bienes', ['Infraestructuras'])

        # Adding model 'Propiedades'
        db.create_table('bienes_propiedades', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bienes.Equipos'], null=True, blank=True)),
            ('cantidad_equipo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('bienes', ['Propiedades'])

        # Adding model 'Infraestructura'
        db.create_table('bienes_infraestructura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('infraestructura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bienes.Infraestructuras'], null=True, blank=True)),
            ('cantidad_infra', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('bienes', ['Infraestructura'])

        # Adding model 'NombreHerramienta'
        db.create_table('bienes_nombreherramienta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bienes', ['NombreHerramienta'])

        # Adding model 'Herramientas'
        db.create_table('bienes_herramientas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('herramienta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bienes.NombreHerramienta'], null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('bienes', ['Herramientas'])

        # Adding model 'NombreTransporte'
        db.create_table('bienes_nombretransporte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bienes', ['NombreTransporte'])

        # Adding model 'Transporte'
        db.create_table('bienes_transporte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transporte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bienes.NombreTransporte'], null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('bienes', ['Transporte'])


    def backwards(self, orm):
        
        # Deleting model 'Casa'
        db.delete_table('bienes_casa')

        # Deleting model 'Piso'
        db.delete_table('bienes_piso')

        # Deleting model 'Techo'
        db.delete_table('bienes_techo')

        # Deleting model 'TipoCasa'
        db.delete_table('bienes_tipocasa')

        # Removing M2M table for field tipo on 'TipoCasa'
        db.delete_table('bienes_tipocasa_tipo')

        # Removing M2M table for field piso on 'TipoCasa'
        db.delete_table('bienes_tipocasa_piso')

        # Removing M2M table for field techo on 'TipoCasa'
        db.delete_table('bienes_tipocasa_techo')

        # Deleting model 'DetalleCasa'
        db.delete_table('bienes_detallecasa')

        # Deleting model 'Equipos'
        db.delete_table('bienes_equipos')

        # Deleting model 'Infraestructuras'
        db.delete_table('bienes_infraestructuras')

        # Deleting model 'Propiedades'
        db.delete_table('bienes_propiedades')

        # Deleting model 'Infraestructura'
        db.delete_table('bienes_infraestructura')

        # Deleting model 'NombreHerramienta'
        db.delete_table('bienes_nombreherramienta')

        # Deleting model 'Herramientas'
        db.delete_table('bienes_herramientas')

        # Deleting model 'NombreTransporte'
        db.delete_table('bienes_nombretransporte')

        # Deleting model 'Transporte'
        db.delete_table('bienes_transporte')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'bienes.casa': {
            'Meta': {'object_name': 'Casa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bienes.detallecasa': {
            'Meta': {'object_name': 'DetalleCasa'},
            'ambientes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letrina': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tamano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'bienes.equipos': {
            'Meta': {'object_name': 'Equipos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bienes.herramientas': {
            'Meta': {'object_name': 'Herramientas'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'herramienta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bienes.NombreHerramienta']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'bienes.infraestructura': {
            'Meta': {'object_name': 'Infraestructura'},
            'cantidad_infra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infraestructura': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bienes.Infraestructuras']", 'null': 'True', 'blank': 'True'})
        },
        'bienes.infraestructuras': {
            'Meta': {'object_name': 'Infraestructuras'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bienes.nombreherramienta': {
            'Meta': {'object_name': 'NombreHerramienta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bienes.nombretransporte': {
            'Meta': {'object_name': 'NombreTransporte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bienes.piso': {
            'Meta': {'object_name': 'Piso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bienes.propiedades': {
            'Meta': {'object_name': 'Propiedades'},
            'cantidad_equipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bienes.Equipos']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bienes.techo': {
            'Meta': {'object_name': 'Techo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bienes.tipocasa': {
            'Meta': {'object_name': 'TipoCasa'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piso': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bienes.Piso']", 'null': 'True', 'blank': 'True'}),
            'techo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bienes.Techo']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bienes.Casa']", 'null': 'True', 'blank': 'True'})
        },
        'bienes.transporte': {
            'Meta': {'object_name': 'Transporte'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transporte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bienes.NombreTransporte']", 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuestas.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'beneficiario': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['encuestas.OrganizacionOCB']", 'null': 'True', 'blank': 'True'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'entrevistado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Recolector']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'encuestas.organizacionocb': {
            'Meta': {'object_name': 'OrganizacionOCB'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuestas.recolector': {
            'Meta': {'object_name': 'Recolector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'lugar.comunidad': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre', 'nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['bienes']
