# Generated by Django 2.2.1 on 2019-06-17 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20190617_0908'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todo',
            new_name='todomodel',
        ),
    ]