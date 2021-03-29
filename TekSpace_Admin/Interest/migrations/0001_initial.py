# Generated by Django 3.1.7 on 2021-03-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('interest_id', models.AutoField(primary_key=True, serialize=False)),
                ('int_name', models.CharField(max_length=20, unique=True)),
                ('int_description', models.CharField(max_length=300)),
                ('int_photo', models.FileField(default='default.png', upload_to='')),
                ('students', models.ManyToManyField(blank=True, to='Students.Student')),
            ],
            options={
                'db_table': 'Interest',
            },
        ),
    ]
