# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Educacion'
        db.create_table('familias_educacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_leer', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('p_incompleta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('p_completa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('s_incompleta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('bachiller', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('universitario', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('f_comunidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('familias', ['Educacion'])

        # Adding model 'PreguntaEnergia'
        db.create_table('familias_preguntaenergia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['PreguntaEnergia'])

        # Adding model 'Energia'
        db.create_table('familias_energia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['familias.PreguntaEnergia'], null=True, blank=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('familias', ['Energia'])

        # Adding model 'TipoCocina'
        db.create_table('familias_tipococina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['TipoCocina'])

        # Adding model 'Cocina'
        db.create_table('familias_cocina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('familias', ['Cocina'])

        # Adding M2M table for field utiliza on 'Cocina'
        db.create_table('familias_cocina_utiliza', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cocina', models.ForeignKey(orm['familias.cocina'], null=False)),
            ('tipococina', models.ForeignKey(orm['familias.tipococina'], null=False))
        ))
        db.create_unique('familias_cocina_utiliza', ['cocina_id', 'tipococina_id'])

        # Adding model 'Fuente'
        db.create_table('familias_fuente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('familias', ['Fuente'])

        # Adding model 'Agua'
        db.create_table('familias_agua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('familias', ['Agua'])

        # Adding M2M table for field fuente on 'Agua'
        db.create_table('familias_agua_fuente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agua', models.ForeignKey(orm['familias.agua'], null=False)),
            ('fuente', models.ForeignKey(orm['familias.fuente'], null=False))
        ))
        db.create_unique('familias_agua_fuente', ['agua_id', 'fuente_id'])


    def backwards(self, orm):
        
        # Deleting model 'Educacion'
        db.delete_table('familias_educacion')

        # Deleting model 'PreguntaEnergia'
        db.delete_table('familias_preguntaenergia')

        # Deleting model 'Energia'
        db.delete_table('familias_energia')

        # Deleting model 'TipoCocina'
        db.delete_table('familias_tipococina')

        # Deleting model 'Cocina'
        db.delete_table('familias_cocina')

        # Removing M2M table for field utiliza on 'Cocina'
        db.delete_table('familias_cocina_utiliza')

        # Deleting model 'Fuente'
        db.delete_table('familias_fuente')

        # Deleting model 'Agua'
        db.delete_table('familias_agua')

        # Removing M2M table for field fuente on 'Agua'
        db.delete_table('familias_agua_fuente')


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
        'familias.agua': {
            'Meta': {'object_name': 'Agua'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'fuente': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['familias.Fuente']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'familias.cocina': {
            'Meta': {'object_name': 'Cocina'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'utiliza': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['familias.TipoCocina']", 'null': 'True', 'blank': 'True'})
        },
        'familias.educacion': {
            'Meta': {'object_name': 'Educacion'},
            'bachiller': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'f_comunidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_leer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'p_completa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'p_incompleta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            's_incompleta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'universitario': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'familias.energia': {
            'Meta': {'object_name': 'Energia'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['familias.PreguntaEnergia']", 'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'familias.fuente': {
            'Meta': {'object_name': 'Fuente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'familias.preguntaenergia': {
            'Meta': {'object_name': 'PreguntaEnergia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'familias.tipococina': {
            'Meta': {'object_name': 'TipoCocina'},
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

    complete_apps = ['familias']
