# Generated by Django 5.0.6 on 2024-05-20 11:50

import core.constants
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("data", "0003_remove_objectsport_object_sport_indoor_outdoor_and_more"),
        ("info", "0004_remove_favoriteevents_events_and_more"),
        ("users", "0002_remove_users_passport_issued_by_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="дата обновления"
                    ),
                ),
                (
                    "news_title",
                    models.CharField(
                        max_length=core.constants.FieldLength["MAX_LENGTH_TITLE"],
                        verbose_name="Название новости",
                    ),
                ),
                (
                    "news_image",
                    models.ImageField(
                        upload_to="images/news/", verbose_name="Фотография"
                    ),
                ),
                ("news_text", models.TextField(verbose_name="Описание новости")),
                (
                    "news_author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="news_author",
                        to="users.users",
                        verbose_name="Автор новости",
                    ),
                ),
                (
                    "news_disciplines",
                    models.ManyToManyField(
                        related_name="news",
                        to="data.disciplines",
                        verbose_name="Дисциплины",
                    ),
                ),
                (
                    "news_regional_divisions",
                    models.ManyToManyField(
                        related_name="news",
                        to="info.regionaldivisions",
                        verbose_name="Региональные отделения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
                "ordering": ["-created_at"],
            },
        ),
    ]