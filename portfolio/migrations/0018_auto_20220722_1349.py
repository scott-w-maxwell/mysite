# Generated by Django 3.2.9 on 2022-07-22 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_auto_20220722_1321'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfilePic',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='resume',
            field=models.FileField(blank=True, upload_to='resumes'),
        ),
    ]
