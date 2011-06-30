# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OrgGremiales'
        db.create_table('organizacion_orggremiales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('organizacion', ['OrgGremiales'])

        # Adding model 'BeneficiosObtenido'
        db.create_table('organizacion_beneficiosobtenido', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('organizacion', ['BeneficiosObtenido'])

        # Adding model 'OrganizacionGremial'
        db.create_table('organizacion_organizaciongremial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desde_socio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('miembro_gremial', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('capacitacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('organizacion', ['OrganizacionGremial'])

        # Adding M2M table for field socio on 'OrganizacionGremial'
        db.create_table('organizacion_organizaciongremial_socio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizaciongremial', models.ForeignKey(orm['organizacion.organizaciongremial'], null=False)),
            ('orggremiales', models.ForeignKey(orm['organizacion.orggremiales'], null=False))
        ))
        db.create_unique('organizacion_organizaciongremial_socio', ['organizaciongremial_id', 'orggremiales_id'])

        # Adding M2M table for field beneficio on 'OrganizacionGremial'
        db.create_table('organizacion_organizaciongremial_beneficio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizaciongremial', models.ForeignKey(orm['organizacion.organizaciongremial'], null=False)),
            ('beneficiosobtenido', models.ForeignKey(orm['organizacion.beneficiosobtenido'], null=False))
        ))
        db.create_unique('organizacion_organizaciongremial_beneficio', ['organizaciongremial_id', 'beneficiosobtenido_id'])

        # Adding model 'OrgComunitarias'
        db.create_table('organizacion_orgcomunitarias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('organizacion', ['OrgComunitarias'])

        # Adding model 'BeneficioOrgComunitaria'
        db.create_table('organizacion_beneficioorgcomunitaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('organizacion', ['BeneficioOrgComunitaria'])

        # Adding model 'NombreOrganizacion'
        db.create_table('organizacion_nombreorganizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('organizacion', ['NombreOrganizacion'])

        # Adding model 'OrganizacionComunitaria'
        db.create_table('organizacion_organizacioncomunitaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pertence', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cuantas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pertence_org', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('personas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('involucradas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('organizacion', ['OrganizacionComunitaria'])

        # Adding M2M table for field cual_organizacion on 'OrganizacionComunitaria'
        db.create_table('organizacion_organizacioncomunitaria_cual_organizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm['organizacion.organizacioncomunitaria'], null=False)),
            ('orgcomunitarias', models.ForeignKey(orm['organizacion.orgcomunitarias'], null=False))
        ))
        db.create_unique('organizacion_organizacioncomunitaria_cual_organizacion', ['organizacioncomunitaria_id', 'orgcomunitarias_id'])

        # Adding M2M table for field cual_beneficio on 'OrganizacionComunitaria'
        db.create_table('organizacion_organizacioncomunitaria_cual_beneficio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm['organizacion.organizacioncomunitaria'], null=False)),
            ('beneficioorgcomunitaria', models.ForeignKey(orm['organizacion.beneficioorgcomunitaria'], null=False))
        ))
        db.create_unique('organizacion_organizacioncomunitaria_cual_beneficio', ['organizacioncomunitaria_id', 'beneficioorgcomunitaria_id'])

        # Adding M2M table for field organizaciones on 'OrganizacionComunitaria'
        db.create_table('organizacion_organizacioncomunitaria_organizaciones', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm['organizacion.organizacioncomunitaria'], null=False)),
            ('nombreorganizacion', models.ForeignKey(orm['organizacion.nombreorganizacion'], null=False))
        ))
        db.create_unique('organizacion_organizacioncomunitaria_organizaciones', ['organizacioncomunitaria_id', 'nombreorganizacion_id'])

        # Adding model 'Tenencia'
        db.create_table('organizacion_tenencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parcela', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dueno', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('organizacion', ['Tenencia'])


    def backwards(self, orm):
        
        # Deleting model 'OrgGremiales'
        db.delete_table('organizacion_orggremiales')

        # Deleting model 'BeneficiosObtenido'
        db.delete_table('organizacion_beneficiosobtenido')

        # Deleting model 'OrganizacionGremial'
        db.delete_table('organizacion_organizaciongremial')

        # Removing M2M table for field socio on 'OrganizacionGremial'
        db.delete_table('organizacion_organizaciongremial_socio')

        # Removing M2M table for field beneficio on 'OrganizacionGremial'
        db.delete_table('organizacion_organizaciongremial_beneficio')

        # Deleting model 'OrgComunitarias'
        db.delete_table('organizacion_orgcomunitarias')

        # Deleting model 'BeneficioOrgComunitaria'
        db.delete_table('organizacion_beneficioorgcomunitaria')

        # Deleting model 'NombreOrganizacion'
        db.delete_table('organizacion_nombreorganizacion')

        # Deleting model 'OrganizacionComunitaria'
        db.delete_table('organizacion_organizacioncomunitaria')

        # Removing M2M table for field cual_organizacion on 'OrganizacionComunitaria'
        db.delete_table('organizacion_organizacioncomunitaria_cual_organizacion')

        # Removing M2M table for field cual_beneficio on 'OrganizacionComunitaria'
        db.delete_table('organizacion_organizacioncomunitaria_cual_beneficio')

        # Removing M2M table for field organizaciones on 'OrganizacionComunitaria'
        db.delete_table('organizacion_organizacioncomunitaria_organizaciones')

        # Deleting model 'Tenencia'
        db.delete_table('organizacion_tenencia')


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
        'organizacion.beneficioorgcomunitaria': {
            'Meta': {'object_name': 'BeneficioOrgComunitaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'organizacion.beneficiosobtenido': {
            'Meta': {'object_name': 'BeneficiosObtenido'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'organizacion.nombreorganizacion': {
            'Meta': {'object_name': 'NombreOrganizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'organizacion.organizacioncomunitaria': {
            'Meta': {'object_name': 'OrganizacionComunitaria'},
            'cual_beneficio': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['organizacion.BeneficioOrgComunitaria']", 'null': 'True', 'blank': 'True'}),
            'cual_organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['organizacion.OrgComunitarias']", 'null': 'True', 'blank': 'True'}),
            'cuantas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'involucradas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'organizaciones': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['organizacion.NombreOrganizacion']", 'null': 'True', 'blank': 'True'}),
            'personas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pertence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pertence_org': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'organizacion.organizaciongremial': {
            'Meta': {'object_name': 'OrganizacionGremial'},
            'beneficio': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['organizacion.BeneficiosObtenido']", 'null': 'True', 'blank': 'True'}),
            'capacitacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'desde_socio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miembro_gremial': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['organizacion.OrgGremiales']", 'null': 'True', 'blank': 'True'})
        },
        'organizacion.orgcomunitarias': {
            'Meta': {'object_name': 'OrgComunitarias'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'organizacion.orggremiales': {
            'Meta': {'object_name': 'OrgGremiales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'organizacion.tenencia': {
            'Meta': {'object_name': 'Tenencia'},
            'dueno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parcela': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['organizacion']
