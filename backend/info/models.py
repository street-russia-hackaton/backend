from core.constants import FieldLength
from data.models import Cities, Disciplines, Regions
from django.db import models
from users.models import Users


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
