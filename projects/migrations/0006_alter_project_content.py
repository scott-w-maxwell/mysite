# Generated by Django 3.2.6 on 2022-04-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
