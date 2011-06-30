# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Productos'
        db.create_table('comercializacion_productos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('comercializacion', ['Productos'])

        # Adding model 'AquienVende'
        db.create_table('comercializacion_aquienvende', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('comercializacion', ['AquienVende'])

        # Adding model 'DondeVende'
        db.create_table('comercializacion_dondevende', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('comercializacion', ['DondeVende'])

        # Adding model 'Comercializacion'
        db.create_table('comercializacion_comercializacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comercializacion.Productos'], null=True, blank=True)),
            ('autoconsumo', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('venta', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('precio', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('comercializacion', ['Comercializacion'])

        # Adding M2M table for field aquien_vende on 'Comercializacion'
        db.create_table('comercializacion_comercializacion_aquien_vende', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comercializacion', models.ForeignKey(orm['comercializacion.comercializacion'], null=False)),
            ('aquienvende', models.ForeignKey(orm['comercializacion.aquienvende'], null=False))
        ))
        db.create_unique('comercializacion_comercializacion_aquien_vende', ['comercializacion_id', 'aquienvende_id'])

        # Adding M2M table for field donde on 'Comercializacion'
        db.create_table('comercializacion_comercializacion_donde', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comercializacion', models.ForeignKey(orm['comercializacion.comercializacion'], null=False)),
            ('dondevende', models.ForeignKey(orm['comercializacion.dondevende'], null=False))
        ))
        db.create_unique('comercializacion_comercializacion_donde', ['comercializacion_id', 'dondevende_id'])

        # Adding model 'Tecnica'
        db.create_table('comercializacion_tecnica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('comercializacion', ['Tecnica'])

        # Adding model 'Familia'
        db.create_table('comercializacion_familia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('comercializacion', ['Familia'])

        # Adding model 'CapacitacionTecnica'
        db.create_table('comercializacion_capacitaciontecnica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('capacitacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comercializacion.Tecnica'], null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('comercializacion', ['CapacitacionTecnica'])

        # Adding M2M table for field respuesta on 'CapacitacionTecnica'
        db.create_table('comercializacion_capacitaciontecnica_respuesta', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('capacitaciontecnica', models.ForeignKey(orm['comercializacion.capacitaciontecnica'], null=False)),
            ('familia', models.ForeignKey(orm['comercializacion.familia'], null=False))
        ))
        db.create_unique('comercializacion_capacitaciontecnica_respuesta', ['capacitaciontecnica_id', 'familia_id'])

        # Adding model 'Social'
        db.create_table('comercializacion_social', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('comercializacion', ['Social'])

        # Adding model 'CapacitacionSocial'
        db.create_table('comercializacion_capacitacionsocial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('capacitacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comercializacion.Social'], null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('comercializacion', ['CapacitacionSocial'])

        # Adding M2M table for field respuesta on 'CapacitacionSocial'
        db.create_table('comercializacion_capacitacionsocial_respuesta', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('capacitacionsocial', models.ForeignKey(orm['comercializacion.capacitacionsocial'], null=False)),
            ('familia', models.ForeignKey(orm['comercializacion.familia'], null=False))
        ))
        db.create_unique('comercializacion_capacitacionsocial_respuesta', ['capacitacionsocial_id', 'familia_id'])


    def backwards(self, orm):
        
        # Deleting model 'Productos'
        db.delete_table('comercializacion_productos')

        # Deleting model 'AquienVende'
        db.delete_table('comercializacion_aquienvende')

        # Deleting model 'DondeVende'
        db.delete_table('comercializacion_dondevende')

        # Deleting model 'Comercializacion'
        db.delete_table('comercializacion_comercializacion')

        # Removing M2M table for field aquien_vende on 'Comercializacion'
        db.delete_table('comercializacion_comercializacion_aquien_vende')

        # Removing M2M table for field donde on 'Comercializacion'
        db.delete_table('comercializacion_comercializacion_donde')

        # Deleting model 'Tecnica'
        db.delete_table('comercializacion_tecnica')

        # Deleting model 'Familia'
        db.delete_table('comercializacion_familia')

        # Deleting model 'CapacitacionTecnica'
        db.delete_table('comercializacion_capacitaciontecnica')

        # Removing M2M table for field respuesta on 'CapacitacionTecnica'
        db.delete_table('comercializacion_capacitaciontecnica_respuesta')

        # Deleting model 'Social'
        db.delete_table('comercializacion_social')

        # Deleting model 'CapacitacionSocial'
        db.delete_table('comercializacion_capacitacionsocial')

        # Removing M2M table for field respuesta on 'CapacitacionSocial'
        db.delete_table('comercializacion_capacitacionsocial_respuesta')


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
        'comercializacion.aquienvende': {
            'Meta': {'object_name': 'AquienVende'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'comercializacion.capacitacionsocial': {
            'Meta': {'object_name': 'CapacitacionSocial'},
            'capacitacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comercializacion.Social']", 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['comercializacion.Familia']", 'null': 'True', 'blank': 'True'})
        },
        'comercializacion.capacitaciontecnica': {
            'Meta': {'object_name': 'CapacitacionTecnica'},
            'capacitacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comercializacion.Tecnica']", 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['comercializacion.Familia']", 'null': 'True', 'blank': 'True'})
        },
        'comercializacion.comercializacion': {
            'Meta': {'object_name': 'Comercializacion'},
            'aquien_vende': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['comercializacion.AquienVende']", 'null': 'True', 'blank': 'True'}),
            'autoconsumo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'donde': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['comercializacion.DondeVende']", 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comercializacion.Productos']", 'null': 'True', 'blank': 'True'}),
            'venta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'comercializacion.dondevende': {
            'Meta': {'object_name': 'DondeVende'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'comercializacion.familia': {
            'Meta': {'object_name': 'Familia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'comercializacion.productos': {
            'Meta': {'object_name': 'Productos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'comercializacion.social': {
            'Meta': {'object_name': 'Social'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'comercializacion.tecnica': {
            'Meta': {'object_name': 'Tecnica'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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

    complete_apps = ['comercializacion']
