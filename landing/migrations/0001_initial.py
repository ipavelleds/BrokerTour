# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tour'
        db.create_table(u'landing_tour', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('nameTour', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('dateDeparture', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('nameHotel', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('aboutHotel', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('starHotel', self.gf('django.db.models.fields.IntegerField')()),
            ('piece', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'landing', ['Tour'])

        # Adding model 'Proposal'
        db.create_table(u'landing_proposal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200, null=True, blank=True)),
            ('tour', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['landing.Tour'], null=True, blank=True)),
        ))
        db.send_create_signal(u'landing', ['Proposal'])


    def backwards(self, orm):
        # Deleting model 'Tour'
        db.delete_table(u'landing_tour')

        # Deleting model 'Proposal'
        db.delete_table(u'landing_proposal')


    models = {
        u'landing.proposal': {
            'Meta': {'object_name': 'Proposal'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tour': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['landing.Tour']", 'null': 'True', 'blank': 'True'})
        },
        u'landing.tour': {
            'Meta': {'object_name': 'Tour'},
            'aboutHotel': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'dateDeparture': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameHotel': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nameTour': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'piece': ('django.db.models.fields.IntegerField', [], {}),
            'starHotel': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['landing']