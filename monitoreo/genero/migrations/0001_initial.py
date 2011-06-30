# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ActividadHogar'
        db.create_table('genero_actividadhogar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('genero', ['ActividadHogar'])

        # Adding model 'ActividadFinca'
        db.create_table('genero_actividadfinca', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('genero', ['ActividadFinca'])

        # Adding model 'Participacion'
        db.create_table('genero_participacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingreso', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('decision', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('proporcion', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('genero', ['Participacion'])

        # Adding M2M table for field principal on 'Participacion'
        db.create_table('genero_participacion_principal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participacion', models.ForeignKey(orm['genero.participacion'], null=False)),
            ('actividadhogar', models.ForeignKey(orm['genero.actividadhogar'], null=False))
        ))
        db.create_unique('genero_participacion_principal', ['participacion_id', 'actividadhogar_id'])

        # Adding M2M table for field actividad_finca on 'Participacion'
        db.create_table('genero_participacion_actividad_finca', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participacion', models.ForeignKey(orm['genero.participacion'], null=False)),
            ('actividadfinca', models.ForeignKey(orm['genero.actividadfinca'], null=False))
        ))
        db.create_unique('genero_participacion_actividad_finca', ['participacion_id', 'actividadfinca_id'])

        # Adding model 'TipoOrganizacion'
        db.create_table('genero_tipoorganizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('genero', ['TipoOrganizacion'])

        # Adding model 'MujerOrganizacion'
        db.create_table('genero_mujerorganizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tipo_organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['genero.TipoOrganizacion'], null=True, blank=True)),
            ('voto', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('reuniones', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('informada', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ideas_familia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ideas_comunidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('genero', ['MujerOrganizacion'])


    def backwards(self, orm):
        
        # Deleting model 'ActividadHogar'
        db.delete_table('genero_actividadhogar')

        # Deleting model 'ActividadFinca'
        db.delete_table('genero_actividadfinca')

        # Deleting model 'Participacion'
        db.delete_table('genero_participacion')

        # Removing M2M table for field principal on 'Participacion'
        db.delete_table('genero_participacion_principal')

        # Removing M2M table for field actividad_finca on 'Participacion'
        db.delete_table('genero_participacion_actividad_finca')

        # Deleting model 'TipoOrganizacion'
        db.delete_table('genero_tipoorganizacion')

        # Deleting model 'MujerOrganizacion'
        db.delete_table('genero_mujerorganizacion')


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
        'genero.actividadfinca': {
            'Meta': {'object_name': 'ActividadFinca'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'genero.actividadhogar': {
            'Meta': {'object_name': 'ActividadHogar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'genero.mujerorganizacion': {
            'Meta': {'object_name': 'MujerOrganizacion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideas_comunidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ideas_familia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'informada': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'participa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reuniones': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['genero.TipoOrganizacion']", 'null': 'True', 'blank': 'True'}),
            'voto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'genero.participacion': {
            'Meta': {'object_name': 'Participacion'},
            'actividad_finca': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['genero.ActividadFinca']", 'null': 'True', 'blank': 'True'}),
            'decision': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingreso': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'principal': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['genero.ActividadHogar']", 'null': 'True', 'blank': 'True'}),
            'proporcion': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'genero.tipoorganizacion': {
            'Meta': {'object_name': 'TipoOrganizacion'},
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

    complete_apps = ['genero']
