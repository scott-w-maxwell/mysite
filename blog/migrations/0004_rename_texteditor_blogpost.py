# Generated by Django 3.2.6 on 2022-04-01 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_texteditor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='textEditor',
            new_name='blogpost',
        ),
    ]
