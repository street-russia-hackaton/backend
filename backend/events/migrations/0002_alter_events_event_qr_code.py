# Generated by Django 5.0.6 on 2024-05-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="event_qr_code",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/events/qr_codes/",
                verbose_name="QR-код",
            ),
        ),
    ]
