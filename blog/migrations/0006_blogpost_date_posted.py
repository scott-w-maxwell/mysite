# Generated by Django 3.2.6 on 2022-04-01 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
