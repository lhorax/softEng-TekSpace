# Generated by Django 3.1.7 on 2021-03-21 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modules', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modules',
            old_name='session_id',
            new_name='session',
        ),
    ]