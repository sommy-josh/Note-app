# Generated by Django 4.0.5 on 2023-04-02 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocha_app', '0002_rename_notes_notebook_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notebook',
            old_name='Notes',
            new_name='notes',
        ),
    ]