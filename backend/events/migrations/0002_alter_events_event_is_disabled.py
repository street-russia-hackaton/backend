# Generated by Django 5.0.6 on 2024-05-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_is_disabled',
            field=models.BooleanField(default=False, verbose_name='Для людей с ограниченными возможностями'),
        ),
    ]
