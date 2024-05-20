# Generated by Django 5.0.6 on 2024-05-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("info", "0005_disciplines_objectsportimage_partners_and_more"),
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="news_disciplines",
            field=models.ManyToManyField(
                related_name="news", to="info.disciplines", verbose_name="Дисциплины"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="news_image",
            field=models.ImageField(
                upload_to="images/news/", verbose_name="Фотография к новости"
            ),
        ),
    ]
