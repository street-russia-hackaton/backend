from core.constants import FieldLength
from django.db import models

from .choice_classes import ObjectTypeChoices, PartnerRoleChoices


class Regions(models.Model):
    region_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE, verbose_name="Название региона"
    )

    def __str__(self):
        return self.region_title

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Cities(models.Model):
    city_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE, verbose_name="Название города"
    )
    city_region = models.ForeignKey(
        Regions, on_delete=models.CASCADE, verbose_name="Регион"
    )

    def __str__(self):
        return self.city_title

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Disciplines(models.Model):
    disciplines_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE, verbose_name="Название дисциплины"
    )
    disciplines_image = models.ImageField(
        upload_to="images/disciplines/", verbose_name="Фотография дисциплины"
    )
    disciplines_video_url = models.URLField(verbose_name="Ссылка на видео")
    disciplines_information = models.TextField(verbose_name="Информация о дисциплине")

    def __str__(self):
        return self.disciplines_title

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class Partners(models.Model):
    partners_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE, verbose_name="Название партнера"
    )
    partners_category = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE,
        choices=PartnerRoleChoices,
        default=PartnerRoleChoices.STRATEGIC,
        verbose_name="Категория партнера",
    )
    partners_logo = models.ImageField(
        upload_to="images/partners/", verbose_name="Логотип партнера"
    )
    partners_url = models.URLField(verbose_name="Ссылка на сайт партнера")

    def __str__(self):
        return self.partners_title

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class ObjectSportImage(models.Model):
    object_sport_image = models.ImageField(
        upload_to="images/object_sport/", verbose_name="Фотография спортивного обьекта"
    )

    def __str__(self):
        return str(self.object_sport_image)

    class Meta:
        verbose_name = "Фотография спортивного обьекта"
        verbose_name_plural = "Фотография спортивных обьектов"


class ObjectSport(models.Model):
    object_sport_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE,
        verbose_name="Название спортивного объекта",
    )
    object_sport_image = models.ManyToManyField(
        ObjectSportImage, verbose_name="Фотография спортивного обьекта"
    )
    object_sport_video = models.URLField(verbose_name="Ссылка на видео объекта спорта")
    object_sport_type = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE,
        choices=ObjectTypeChoices,
        default=ObjectTypeChoices.INDOOR,
        verbose_name="Помещение (закрытое/открытое)",
    )
    object_sport_info = models.TextField(verbose_name="Описание объекта")
    object_disciplines = models.ManyToManyField(
        Disciplines, verbose_name="Дисциплины объекта"
    )
    object_sport_address = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE, verbose_name="Адрес обьекта"
    )

    def __str__(self):
        return self.object_sport_title

    class Meta:
        verbose_name = "Спортивный объект"
        verbose_name_plural = "Спортивные объекты"
