# Generated by Django 5.0.6 on 2024-05-16 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objectsport',
            old_name='video_object_sport',
            new_name='object_sport_video',
        ),
    ]
