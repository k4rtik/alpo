# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table(u'quotes_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('program', self.gf('django.db.models.fields.CharField')(default='BCS', max_length=3)),
            ('class_of', self.gf('django.db.models.fields.IntegerField')()),
            ('submission_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'quotes', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table(u'quotes_quote')


    models = {
        u'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'class_of': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.CharField', [], {'default': "'BCS'", 'max_length': '3'}),
            'submission_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quotes']