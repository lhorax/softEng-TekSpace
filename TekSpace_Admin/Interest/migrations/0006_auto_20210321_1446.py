# Generated by Django 3.1.7 on 2021-03-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interest', '0005_auto_20210321_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='int_description',
            field=models.CharField(max_length=300),
        ),
    ]