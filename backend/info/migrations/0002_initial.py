# Generated by Django 5.0.6 on 2024-05-26 18:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("data", "0001_initial"),
        ("info", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="donats",
            name="email",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="donats_email",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Электронная почта для доната",
            ),
        ),
        migrations.AddField(
            model_name="donats",
            name="phone",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="donats_phone",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Номер телефона для доната",
            ),
        ),
        migrations.AddField(
            model_name="objectsport",
            name="object_disciplines",
            field=models.ManyToManyField(
                to="info.disciplines", verbose_name="Дисциплины объекта"
            ),
        ),
        migrations.AddField(
            model_name="objectsport",
            name="object_sport_image",
            field=models.ManyToManyField(
                to="info.objectsportimage",
                verbose_name="Фотография спортивного обьекта",
            ),
        ),
        migrations.AddField(
            model_name="regionaldivisions",
            name="regional_divisions_curator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="regional_divisions",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Руководитель регионального отделения",
            ),
        ),
        migrations.AddField(
            model_name="regionaldivisions",
            name="regional_divisions_discipline",
            field=models.ManyToManyField(
                related_name="regional_divisions",
                to="info.disciplines",
                verbose_name="Дисциплина",
            ),
        ),
        migrations.AddField(
            model_name="regionaldivisions",
            name="regional_divisions_region",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="regional_divisions",
                to="data.regions",
                verbose_name="Регион",
            ),
        ),
        migrations.AddField(
            model_name="regionaldivisions",
            name="regional_divisions_sport_obj",
            field=models.ManyToManyField(
                related_name="regional_sport_objects",
                to="info.objectsport",
                verbose_name="Спортивные объекты",
            ),
        ),
        migrations.AddField(
            model_name="regionaldivisions",
            name="regional_divisions_сity",
            field=models.ManyToManyField(
                related_name="regional_divisions",
                to="data.cities",
                verbose_name="Список городов",
            ),
        ),
    ]
