# Generated by Django 2.2.5 on 2020-02-07 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='websites',
            old_name='users',
            new_name='userw',
        ),
    ]