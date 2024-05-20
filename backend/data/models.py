from core.constants import FieldLength
from django.db import models


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
