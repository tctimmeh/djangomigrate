# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models, migrations
from django.db.migrations import RunPython

def createData(apps, schema_editor):
  SomeData = apps.get_model('mtestapp', 'SomeData')
  db_alias = schema_editor.connection.alias
  SomeData.objects.using(db_alias).bulk_create([
      SomeData(value = 1),
  ])

class Migration(migrations.Migration):

    dependencies = [
        ('mtestapp', '0001_initial'),
    ]

    operations = [
        RunPython(createData)
    ]
