# Generated by Django 2.2.1 on 2019-06-19 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_auto_20190617_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
