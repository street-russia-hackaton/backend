from core.constants import FieldLength
from data.models import Cities, Regions
from django.db import models
from users.models import Users

from .choice_classes import ObjectTypeChoices, PartnerRoleChoices


class Disciplines(models.Model):
    disciplines_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE, verbose_name="Название дисциплины"
    )
    disciplines_image = models.ImageField(
        upload_to="images/disciplines/", verbose_name="Фотография дисциплины"
    )
    disciplines_video_url = models.URLField(verbose_name="Ссылка на видео", blank=True)
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
    partners_url = models.URLField(
        verbose_name="Ссылка на сайт партнера",
        blank=True,
    )

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
    object_sport_video = models.URLField(
        verbose_name="Ссылка на видео объекта спорта", blank=True
    )
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


class RegionalDivisions(models.Model):
    regional_divisions_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE,
        verbose_name="Название регионального отделения",
    )
    regional_divisions_image = models.ImageField(
        upload_to="images/regional_divisions/",
        verbose_name="Фотографии региональных отделений",
    )
    regional_divisions_information = models.TextField(
        verbose_name="Общая информация регионального отделения"
    )
    regional_divisions_info = models.TextField(
        verbose_name="Описание регионального отделения"
    )
    regional_divisions_сity = models.ManyToManyField(
        Cities, verbose_name="Список городов", related_name="regional_divisions"
    )
    regional_divisions_region = models.OneToOneField(
        Regions,
        on_delete=models.CASCADE,
        verbose_name="Регион",
        related_name="regional_divisions",
    )
    regional_divisions_sport_obj = models.ManyToManyField(
        ObjectSport,
        verbose_name="Спортивные объекты",
        related_name="regional_sport_objects",
    )
    regional_divisions_discipline = models.ManyToManyField(
        Disciplines, verbose_name="Дисциплина", related_name="regional_divisions"
    )
    regional_divisions_curator = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Руководитель регионального отделения",
        related_name="regional_divisions",
    )

    def __str__(self):
        return self.regional_divisions_title

    class Meta:
        verbose_name = "Региональное отделение"
        verbose_name_plural = "Региональные отделения"


class Donats(models.Model):
    email = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="donats_email",
        verbose_name="Электронная почта для доната",
    )
    phone = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="donats_phone",
        verbose_name="Номер телефона для доната",
    )
    donats_sum = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма доната"
    )
    terms_agreed = models.BooleanField(
        default=False, verbose_name="Согласие на договор-оферты"
    )

    def __str__(self):
        return f"{self.email} - {self.phone} - {self.donats_sum}"

    class Meta:
        verbose_name = "Донат"
        verbose_name_plural = "Донаты"
