# Generated by Django 3.1.7 on 2021-03-21 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20210321_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='profile',
            new_name='profile_picture',
        ),
    ]