# Generated by Django 3.2.6 on 2022-04-04 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20220403_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
