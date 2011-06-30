# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Textura'
        db.create_table('suelo_textura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('suelo', ['Textura'])

        # Adding model 'Profundidad'
        db.create_table('suelo_profundidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('suelo', ['Profundidad'])

        # Adding model 'Densidad'
        db.create_table('suelo_densidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('suelo', ['Densidad'])

        # Adding model 'Pendiente'
        db.create_table('suelo_pendiente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('suelo', ['Pendiente'])

        # Adding model 'Drenaje'
        db.create_table('suelo_drenaje', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('suelo', ['Drenaje'])

        # Adding model 'Suelo'
        db.create_table('suelo_suelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('suelo', ['Suelo'])

        # Adding M2M table for field textura on 'Suelo'
        db.create_table('suelo_suelo_textura', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['suelo.suelo'], null=False)),
            ('textura', models.ForeignKey(orm['suelo.textura'], null=False))
        ))
        db.create_unique('suelo_suelo_textura', ['suelo_id', 'textura_id'])

        # Adding M2M table for field profundidad on 'Suelo'
        db.create_table('suelo_suelo_profundidad', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['suelo.suelo'], null=False)),
            ('profundidad', models.ForeignKey(orm['suelo.profundidad'], null=False))
        ))
        db.create_unique('suelo_suelo_profundidad', ['suelo_id', 'profundidad_id'])

        # Adding M2M table for field lombrices on 'Suelo'
        db.create_table('suelo_suelo_lombrices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['suelo.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm['suelo.densidad'], null=False))
        ))
        db.create_unique('suelo_suelo_lombrices', ['suelo_id', 'densidad_id'])

        # Adding M2M table for field densidad on 'Suelo'
        db.create_table('suelo_suelo_densidad', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['suelo.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm['suelo.densidad'], null=False))
        ))
        db.create_unique('suelo_suelo_densidad', ['suelo_id', 'densidad_id'])

        # Adding M2M table for field pendiente on 'Suelo'
        db.create_table('suelo_suelo_pendiente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['suelo.suelo'], null=False)),
            ('pendiente', models.ForeignKey(orm['suelo.pendiente'], null=False))
        ))
        db.create_unique('suelo_suelo_pendiente', ['suelo_id', 'pendiente_id'])

        # Adding M2M table for field drenaje on 'Suelo'
        db.create_table('suelo_suelo_drenaje', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['suelo.suelo'], null=False)),
            ('drenaje', models.ForeignKey(orm['suelo.drenaje'], null=False))
        ))
        db.create_unique('suelo_suelo_drenaje', ['suelo_id', 'drenaje_id'])

        # Adding M2M table for field materia on 'Suelo'
        db.create_table('suelo_suelo_materia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['suelo.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm['suelo.densidad'], null=False))
        ))
        db.create_unique('suelo_suelo_materia', ['suelo_id', 'densidad_id'])

        # Adding model 'Preparar'
        db.create_table('suelo_preparar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('suelo', ['Preparar'])

        # Adding model 'Traccion'
        db.create_table('suelo_traccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('suelo', ['Traccion'])

        # Adding model 'Fertilizacion'
        db.create_table('suelo_fertilizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('suelo', ['Fertilizacion'])

        # Adding model 'Conservacion'
        db.create_table('suelo_conservacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('suelo', ['Conservacion'])

        # Adding model 'ManejoSuelo'
        db.create_table('suelo_manejosuelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analisis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('practica', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('suelo', ['ManejoSuelo'])

        # Adding M2M table for field preparan on 'ManejoSuelo'
        db.create_table('suelo_manejosuelo_preparan', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['suelo.manejosuelo'], null=False)),
            ('preparar', models.ForeignKey(orm['suelo.preparar'], null=False))
        ))
        db.create_unique('suelo_manejosuelo_preparan', ['manejosuelo_id', 'preparar_id'])

        # Adding M2M table for field traccion on 'ManejoSuelo'
        db.create_table('suelo_manejosuelo_traccion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['suelo.manejosuelo'], null=False)),
            ('traccion', models.ForeignKey(orm['suelo.traccion'], null=False))
        ))
        db.create_unique('suelo_manejosuelo_traccion', ['manejosuelo_id', 'traccion_id'])

        # Adding M2M table for field fertilizacion on 'ManejoSuelo'
        db.create_table('suelo_manejosuelo_fertilizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['suelo.manejosuelo'], null=False)),
            ('fertilizacion', models.ForeignKey(orm['suelo.fertilizacion'], null=False))
        ))
        db.create_unique('suelo_manejosuelo_fertilizacion', ['manejosuelo_id', 'fertilizacion_id'])

        # Adding M2M table for field obra on 'ManejoSuelo'
        db.create_table('suelo_manejosuelo_obra', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['suelo.manejosuelo'], null=False)),
            ('conservacion', models.ForeignKey(orm['suelo.conservacion'], null=False))
        ))
        db.create_unique('suelo_manejosuelo_obra', ['manejosuelo_id', 'conservacion_id'])


    def backwards(self, orm):
        
        # Deleting model 'Textura'
        db.delete_table('suelo_textura')

        # Deleting model 'Profundidad'
        db.delete_table('suelo_profundidad')

        # Deleting model 'Densidad'
        db.delete_table('suelo_densidad')

        # Deleting model 'Pendiente'
        db.delete_table('suelo_pendiente')

        # Deleting model 'Drenaje'
        db.delete_table('suelo_drenaje')

        # Deleting model 'Suelo'
        db.delete_table('suelo_suelo')

        # Removing M2M table for field textura on 'Suelo'
        db.delete_table('suelo_suelo_textura')

        # Removing M2M table for field profundidad on 'Suelo'
        db.delete_table('suelo_suelo_profundidad')

        # Removing M2M table for field lombrices on 'Suelo'
        db.delete_table('suelo_suelo_lombrices')

        # Removing M2M table for field densidad on 'Suelo'
        db.delete_table('suelo_suelo_densidad')

        # Removing M2M table for field pendiente on 'Suelo'
        db.delete_table('suelo_suelo_pendiente')

        # Removing M2M table for field drenaje on 'Suelo'
        db.delete_table('suelo_suelo_drenaje')

        # Removing M2M table for field materia on 'Suelo'
        db.delete_table('suelo_suelo_materia')

        # Deleting model 'Preparar'
        db.delete_table('suelo_preparar')

        # Deleting model 'Traccion'
        db.delete_table('suelo_traccion')

        # Deleting model 'Fertilizacion'
        db.delete_table('suelo_fertilizacion')

        # Deleting model 'Conservacion'
        db.delete_table('suelo_conservacion')

        # Deleting model 'ManejoSuelo'
        db.delete_table('suelo_manejosuelo')

        # Removing M2M table for field preparan on 'ManejoSuelo'
        db.delete_table('suelo_manejosuelo_preparan')

        # Removing M2M table for field traccion on 'ManejoSuelo'
        db.delete_table('suelo_manejosuelo_traccion')

        # Removing M2M table for field fertilizacion on 'ManejoSuelo'
        db.delete_table('suelo_manejosuelo_fertilizacion')

        # Removing M2M table for field obra on 'ManejoSuelo'
        db.delete_table('suelo_manejosuelo_obra')


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
        'suelo.conservacion': {
            'Meta': {'object_name': 'Conservacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'suelo.densidad': {
            'Meta': {'object_name': 'Densidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'suelo.drenaje': {
            'Meta': {'object_name': 'Drenaje'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'suelo.fertilizacion': {
            'Meta': {'object_name': 'Fertilizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'suelo.manejosuelo': {
            'Meta': {'object_name': 'ManejoSuelo'},
            'analisis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'fertilizacion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['suelo.Fertilizacion']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obra': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['suelo.Conservacion']", 'null': 'True', 'blank': 'True'}),
            'practica': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'preparan': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['suelo.Preparar']", 'null': 'True', 'blank': 'True'}),
            'traccion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['suelo.Traccion']", 'null': 'True', 'blank': 'True'})
        },
        'suelo.pendiente': {
            'Meta': {'object_name': 'Pendiente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'suelo.preparar': {
            'Meta': {'object_name': 'Preparar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'suelo.profundidad': {
            'Meta': {'object_name': 'Profundidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'suelo.suelo': {
            'Meta': {'object_name': 'Suelo'},
            'densidad': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'densidad'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['suelo.Densidad']"}),
            'drenaje': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['suelo.Drenaje']", 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lombrices': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'lombrices'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['suelo.Densidad']"}),
            'materia': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'materia'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['suelo.Densidad']"}),
            'pendiente': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['suelo.Pendiente']", 'null': 'True', 'blank': 'True'}),
            'profundidad': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['suelo.Profundidad']", 'null': 'True', 'blank': 'True'}),
            'textura': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['suelo.Textura']", 'null': 'True', 'blank': 'True'})
        },
        'suelo.textura': {
            'Meta': {'object_name': 'Textura'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'suelo.traccion': {
            'Meta': {'object_name': 'Traccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['suelo']
