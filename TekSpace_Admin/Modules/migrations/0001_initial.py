# Generated by Django 3.1.7 on 2021-03-27 01:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('mod_ID', models.AutoField(primary_key=True, serialize=False)),
                ('modulename', models.CharField(max_length=50)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sessions.session')),
            ],
            options={
                'db_table': 'modules',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('modules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Modules.module')),
            ],
            options={
                'db_table': 'files',
            },
        ),
    ]