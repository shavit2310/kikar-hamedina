# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TagSynonym'
        db.create_table(u'kikartags_tagsynonym', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proper_form_of_tag', unique=True, to=orm['kikartags.Tag'])),
            ('proper_form_of_tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='synonyms', to=orm['kikartags.Tag'])),
        ))
        db.send_create_signal(u'kikartags', ['TagSynonym'])

        # Adding unique constraint on 'TagSynonym', fields ['tag', 'proper_form_of_tag']
        db.create_unique(u'kikartags_tagsynonym', ['tag_id', 'proper_form_of_tag_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'TagSynonym', fields ['tag', 'proper_form_of_tag']
        db.delete_unique(u'kikartags_tagsynonym', ['tag_id', 'proper_form_of_tag_id'])

        # Deleting model 'TagSynonym'
        db.delete_table(u'kikartags_tagsynonym')


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
        u'kikartags.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_for_main_display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_suggestion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'kikartags.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'kikartags_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            'date_of_tagging': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 16, 0, 0)', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'kikartags_taggeditem_items'", 'to': u"orm['kikartags.Tag']"}),
            'tagged_by': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'tagged'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'kikartags.tagsynonym': {
            'Meta': {'unique_together': "(('tag', 'proper_form_of_tag'),)", 'object_name': 'TagSynonym'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proper_form_of_tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'synonyms'", 'to': u"orm['kikartags.Tag']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proper_form_of_tag'", 'unique': 'True', 'to': u"orm['kikartags.Tag']"})
        }
    }

    complete_apps = ['kikartags']