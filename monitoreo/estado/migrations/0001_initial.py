# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Vivero'
        db.create_table('estado_vivero', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vivero_cacao', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('edad_planta', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('plantas', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('planta_injerto', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['Vivero'])

        # Adding model 'PlantaDesarrolloMenos'
        db.create_table('estado_plantadesarrollomenos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cacao_desarrollo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('edad_planta', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area_sembrada', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('plantas_finca', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('planta_injerto', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['PlantaDesarrolloMenos'])

        # Adding model 'PlantaDesarrolloMas'
        db.create_table('estado_plantadesarrollomas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cacao_desarrollo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('edad_planta', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area_sembrada', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('plantas_finca', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('planta_injerto', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['PlantaDesarrolloMas'])

        # Adding model 'PlantaProduccion'
        db.create_table('estado_plantaproduccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plantas_cacao', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('edad_planta', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area_sembrada', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('plantas_finca', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('planta_injerto', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('sin_fermentar', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('fermentado', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('organico', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['PlantaProduccion'])

        # Adding model 'PlantaElite'
        db.create_table('estado_plantaelite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('elite', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('edad_planta', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cuantas', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['PlantaElite'])

        # Adding model 'Costo'
        db.create_table('estado_costo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mantenimiento_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mantenimiento_finca', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['Costo'])

        # Adding model 'Practicas'
        db.create_table('estado_practicas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('estado', ['Practicas'])

        # Adding model 'ViveroPractica'
        db.create_table('estado_viveropractica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('practica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estado.Practicas'], null=True, blank=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['ViveroPractica'])

        # Adding model 'PracticaEtapa'
        db.create_table('estado_practicaetapa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('estado', ['PracticaEtapa'])

        # Adding model 'PracticaFertilizacion'
        db.create_table('estado_practicafertilizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('practica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estado.PracticaEtapa'], null=True, blank=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['PracticaFertilizacion'])

        # Adding model 'PracticaFitosanitaria'
        db.create_table('estado_practicafitosanitaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('estado', ['PracticaFitosanitaria'])

        # Adding model 'PracticaManejoFitosanitario'
        db.create_table('estado_practicamanejofitosanitario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('practica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estado.PracticaFitosanitaria'], null=True, blank=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['PracticaManejoFitosanitario'])

        # Adding model 'PracticaProductivo'
        db.create_table('estado_practicaproductivo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('estado', ['PracticaProductivo'])

        # Adding model 'PracticaManejoProductivo'
        db.create_table('estado_practicamanejoproductivo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('practica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estado.PracticaProductivo'], null=True, blank=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['PracticaManejoProductivo'])

        # Adding model 'PracticaGenetico'
        db.create_table('estado_practicagenetico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('estado', ['PracticaGenetico'])

        # Adding model 'PracticaMejoramientoGenetico'
        db.create_table('estado_practicamejoramientogenetico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('practica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estado.PracticaGenetico'], null=True, blank=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['PracticaMejoramientoGenetico'])

        # Adding model 'PracticaPostcosecha'
        db.create_table('estado_practicapostcosecha', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('estado', ['PracticaPostcosecha'])

        # Adding model 'PracticaManejoPostcosecha'
        db.create_table('estado_practicamanejopostcosecha', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('practica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estado.PracticaPostcosecha'], null=True, blank=True)),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['PracticaManejoPostcosecha'])

        # Adding model 'Niveles'
        db.create_table('estado_niveles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nivel_fermentacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nivel_secado', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('centro_acopio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('socio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuesta'])),
        ))
        db.send_create_signal('estado', ['Niveles'])


    def backwards(self, orm):
        
        # Deleting model 'Vivero'
        db.delete_table('estado_vivero')

        # Deleting model 'PlantaDesarrolloMenos'
        db.delete_table('estado_plantadesarrollomenos')

        # Deleting model 'PlantaDesarrolloMas'
        db.delete_table('estado_plantadesarrollomas')

        # Deleting model 'PlantaProduccion'
        db.delete_table('estado_plantaproduccion')

        # Deleting model 'PlantaElite'
        db.delete_table('estado_plantaelite')

        # Deleting model 'Costo'
        db.delete_table('estado_costo')

        # Deleting model 'Practicas'
        db.delete_table('estado_practicas')

        # Deleting model 'ViveroPractica'
        db.delete_table('estado_viveropractica')

        # Deleting model 'PracticaEtapa'
        db.delete_table('estado_practicaetapa')

        # Deleting model 'PracticaFertilizacion'
        db.delete_table('estado_practicafertilizacion')

        # Deleting model 'PracticaFitosanitaria'
        db.delete_table('estado_practicafitosanitaria')

        # Deleting model 'PracticaManejoFitosanitario'
        db.delete_table('estado_practicamanejofitosanitario')

        # Deleting model 'PracticaProductivo'
        db.delete_table('estado_practicaproductivo')

        # Deleting model 'PracticaManejoProductivo'
        db.delete_table('estado_practicamanejoproductivo')

        # Deleting model 'PracticaGenetico'
        db.delete_table('estado_practicagenetico')

        # Deleting model 'PracticaMejoramientoGenetico'
        db.delete_table('estado_practicamejoramientogenetico')

        # Deleting model 'PracticaPostcosecha'
        db.delete_table('estado_practicapostcosecha')

        # Deleting model 'PracticaManejoPostcosecha'
        db.delete_table('estado_practicamanejopostcosecha')

        # Deleting model 'Niveles'
        db.delete_table('estado_niveles')


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
        'estado.costo': {
            'Meta': {'object_name': 'Costo'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mantenimiento_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mantenimiento_finca': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.niveles': {
            'Meta': {'object_name': 'Niveles'},
            'centro_acopio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_fermentacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nivel_secado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'socio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.plantadesarrollomas': {
            'Meta': {'object_name': 'PlantaDesarrolloMas'},
            'area_sembrada': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cacao_desarrollo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'edad_planta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'planta_injerto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plantas_finca': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.plantadesarrollomenos': {
            'Meta': {'object_name': 'PlantaDesarrolloMenos'},
            'area_sembrada': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cacao_desarrollo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'edad_planta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'planta_injerto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plantas_finca': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.plantaelite': {
            'Meta': {'object_name': 'PlantaElite'},
            'cuantas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'edad_planta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'elite': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'estado.plantaproduccion': {
            'Meta': {'object_name': 'PlantaProduccion'},
            'area_sembrada': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'edad_planta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'fermentado': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organico': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'planta_injerto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plantas_cacao': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'plantas_finca': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sin_fermentar': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.practicaetapa': {
            'Meta': {'object_name': 'PracticaEtapa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'estado.practicafertilizacion': {
            'Meta': {'object_name': 'PracticaFertilizacion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'practica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estado.PracticaEtapa']", 'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.practicafitosanitaria': {
            'Meta': {'object_name': 'PracticaFitosanitaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'estado.practicagenetico': {
            'Meta': {'object_name': 'PracticaGenetico'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'estado.practicamanejofitosanitario': {
            'Meta': {'object_name': 'PracticaManejoFitosanitario'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'practica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estado.PracticaFitosanitaria']", 'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.practicamanejopostcosecha': {
            'Meta': {'object_name': 'PracticaManejoPostcosecha'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'practica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estado.PracticaPostcosecha']", 'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.practicamanejoproductivo': {
            'Meta': {'object_name': 'PracticaManejoProductivo'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'practica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estado.PracticaProductivo']", 'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.practicamejoramientogenetico': {
            'Meta': {'object_name': 'PracticaMejoramientoGenetico'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'practica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estado.PracticaGenetico']", 'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.practicapostcosecha': {
            'Meta': {'object_name': 'PracticaPostcosecha'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'estado.practicaproductivo': {
            'Meta': {'object_name': 'PracticaProductivo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'estado.practicas': {
            'Meta': {'object_name': 'Practicas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'estado.vivero': {
            'Meta': {'object_name': 'Vivero'},
            'edad_planta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'planta_injerto': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plantas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vivero_cacao': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'estado.viveropractica': {
            'Meta': {'object_name': 'ViveroPractica'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'practica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estado.Practicas']", 'null': 'True', 'blank': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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

    complete_apps = ['estado']
