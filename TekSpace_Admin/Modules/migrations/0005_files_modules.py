# Generated by Django 3.1.7 on 2021-03-21 07:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Modules', '0004_auto_20210321_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
            ],
            options={
                'db_table': 'files',
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('mod_ID', models.AutoField(primary_key=True, serialize=False)),
                ('modulename', models.CharField(max_length=200)),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Modules.files')),
            ],
            options={
                'db_table': 'modules',
            },
        ),
    ]