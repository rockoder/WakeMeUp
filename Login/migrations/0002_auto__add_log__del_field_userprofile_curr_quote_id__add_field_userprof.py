# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Log'
        db.create_table(u'login_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['login.UserProfile'])),
            ('quote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['login.Quote'])),
            ('wake_up_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'login', ['Log'])

        # Deleting field 'UserProfile.curr_quote_id'
        db.delete_column(u'login_userprofile', 'curr_quote_id')

        # Adding field 'UserProfile.prev_login_time'
        db.add_column(u'login_userprofile', 'prev_login_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 15, 0, 0)),
                      keep_default=False)

        # Adding field 'Quote.meta_data'
        db.add_column(u'login_quote', 'meta_data',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Log'
        db.delete_table(u'login_log')

        # Adding field 'UserProfile.curr_quote_id'
        db.add_column(u'login_userprofile', 'curr_quote_id',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'UserProfile.prev_login_time'
        db.delete_column(u'login_userprofile', 'prev_login_time')

        # Deleting field 'Quote.meta_data'
        db.delete_column(u'login_quote', 'meta_data')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'login.log': {
            'Meta': {'object_name': 'Log'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['login.Quote']"}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['login.UserProfile']"}),
            'wake_up_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'login.quote': {
            'Meta': {'object_name': 'Quote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.TextField', [], {})
        },
        u'login.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prev_login_time': ('django.db.models.fields.DateTimeField', [], {}),
            'time_zone': ('timezone_field.fields.TimeZoneField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'wake_up_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['login']