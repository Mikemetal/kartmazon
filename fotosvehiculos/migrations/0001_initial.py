# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fotosvehiculos'
        db.create_table(u'fotosvehiculos_fotosvehiculos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vehiculo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fotosvehiculos', to=orm['vehiculos.Vehiculos'])),
            ('path', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'fotosvehiculos', ['Fotosvehiculos'])


    def backwards(self, orm):
        # Deleting model 'Fotosvehiculos'
        db.delete_table(u'fotosvehiculos_fotosvehiculos')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fotosvehiculos.fotosvehiculos': {
            'Meta': {'object_name': 'Fotosvehiculos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'vehiculo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fotosvehiculos'", 'to': u"orm['vehiculos.Vehiculos']"})
        },
        u'marca.marca': {
            'Meta': {'object_name': 'Marca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        u'modelo.modelo': {
            'Meta': {'object_name': 'Modelo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'marca'", 'to': u"orm['marca.Marca']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        u'tipovehiculo.tipovehiculo': {
            'Meta': {'object_name': 'Tipovehiculo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        u'vehiculos.vehiculos': {
            'Meta': {'object_name': 'Vehiculos'},
            'contador': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kilometraje': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'modelo'", 'to': u"orm['modelo.Modelo']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '0', 'blank': 'True'}),
            'tipovehiculo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'tipovehiculo'", 'to': u"orm['tipovehiculo.Tipovehiculo']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'usuario'", 'to': u"orm['auth.User']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fotosvehiculos']