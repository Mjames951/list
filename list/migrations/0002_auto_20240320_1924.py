# Generated by Django 3.2.24 on 2024-03-21 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='address',
            new_name='home_address',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='tier',
            new_name='membership_tier',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='mode_of_contact',
            new_name='preferred_mode_of_contact',
        ),
    ]
