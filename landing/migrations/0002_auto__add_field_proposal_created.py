# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Proposal.created'
        db.add_column(u'landing_proposal', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 12, 15, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Proposal.created'
        db.delete_column(u'landing_proposal', 'created')


    models = {
        u'landing.proposal': {
            'Meta': {'object_name': 'Proposal'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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