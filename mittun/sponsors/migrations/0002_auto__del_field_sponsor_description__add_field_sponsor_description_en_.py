# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Sponsor.description'
        db.delete_column('sponsors_sponsor', 'description')

        # Adding field 'Sponsor.description_en_us'
        db.add_column('sponsors_sponsor', 'description_en_us', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'Sponsor.description_pt_br'
        db.add_column('sponsors_sponsor', 'description_pt_br', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Deleting field 'Category.name'
        db.delete_column('sponsors_category', 'name')

        # Adding field 'Category.name_en_us'
        db.add_column('sponsors_category', 'name_en_us', self.gf('django.db.models.fields.CharField')(default='', max_length=120), keep_default=False)

        # Adding field 'Category.name_pt_br'
        db.add_column('sponsors_category', 'name_pt_br', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Sponsor.description'
        db.add_column('sponsors_sponsor', 'description', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Deleting field 'Sponsor.description_en_us'
        db.delete_column('sponsors_sponsor', 'description_en_us')

        # Deleting field 'Sponsor.description_pt_br'
        db.delete_column('sponsors_sponsor', 'description_pt_br')

        # Adding field 'Category.name'
        db.add_column('sponsors_category', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=120), keep_default=False)

        # Deleting field 'Category.name_en_us'
        db.delete_column('sponsors_category', 'name_en_us')

        # Deleting field 'Category.name_pt_br'
        db.delete_column('sponsors_category', 'name_pt_br')


    models = {
        'sponsors.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en_us': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'name_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        },
        'sponsors.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Sponsor']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sponsors.Category']"}),
            'description_en_us': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description_pt_br': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['sponsors']
