# Generated by Django 3.2.9 on 2022-07-22 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_aboutme_work_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='work_experience',
        ),
    ]
