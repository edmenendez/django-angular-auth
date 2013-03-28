# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PaymentType'
        db.create_table(u'myproperty_paymenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal(u'myproperty', ['PaymentType'])


    def backwards(self, orm):
        # Deleting model 'PaymentType'
        db.delete_table(u'myproperty_paymenttype')


    models = {
        u'myproperty.paymenttype': {
            'Meta': {'object_name': 'PaymentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        }
    }

    complete_apps = ['myproperty']