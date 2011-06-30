# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Causa'
        db.create_table('riesgos_causa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('riesgos', ['Causa'])

        # Adding model 'Fenomeno'
        db.create_table('riesgos_fenomeno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('causa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riesgos.Causa'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('riesgos', ['Fenomeno'])

        # Adding model 'Graves'
        db.create_table('riesgos_graves', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('riesgos', ['Graves'])

        # Adding model 'Vulnerable'
        db.create_table('riesgos_vulnerable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('motivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riesgos.Fenomeno'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('riesgos', ['Vulnerable'])

        # Adding M2M table for field respuesta on 'Vulnerable'
        db.create_table('riesgos_vulnerable_respuesta', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vulnerable', models.ForeignKey(orm['riesgos.vulnerable'], null=False)),
            ('graves', models.ForeignKey(orm['riesgos.graves'], null=False))
        ))
        db.create_unique('riesgos_vulnerable_respuesta', ['vulnerable_id', 'graves_id'])

        # Adding model 'PreguntaRiesgo'
        db.create_table('riesgos_preguntariesgo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('riesgos', ['PreguntaRiesgo'])

        # Adding model 'Riesgos'
        db.create_table('riesgos_riesgos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riesgos.PreguntaRiesgo'], null=True, blank=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('riesgos', ['Riesgos'])


    def backwards(self, orm):
        
        # Deleting model 'Causa'
        db.delete_table('riesgos_causa')

        # Deleting model 'Fenomeno'
        db.delete_table('riesgos_fenomeno')

        # Deleting model 'Graves'
        db.delete_table('riesgos_graves')

        # Deleting model 'Vulnerable'
        db.delete_table('riesgos_vulnerable')

        # Removing M2M table for field respuesta on 'Vulnerable'
        db.delete_table('riesgos_vulnerable_respuesta')

        # Deleting model 'PreguntaRiesgo'
        db.delete_table('riesgos_preguntariesgo')

        # Deleting model 'Riesgos'
        db.delete_table('riesgos_riesgos')


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
        },
        'riesgos.causa': {
            'Meta': {'object_name': 'Causa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'riesgos.fenomeno': {
            'Meta': {'object_name': 'Fenomeno'},
            'causa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riesgos.Causa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'riesgos.graves': {
            'Meta': {'object_name': 'Graves'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'riesgos.preguntariesgo': {
            'Meta': {'object_name': 'PreguntaRiesgo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'riesgos.riesgos': {
            'Meta': {'object_name': 'Riesgos'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riesgos.PreguntaRiesgo']", 'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'riesgos.vulnerable': {
            'Meta': {'object_name': 'Vulnerable'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riesgos.Fenomeno']"}),
            'respuesta': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['riesgos.Graves']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['riesgos']
