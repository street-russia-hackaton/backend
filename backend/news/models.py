from core.constants import FieldLength
from core.models import TimeStamp
from data.models import Cities
from django.db import models
from info.models import Disciplines, RegionalDivisions
from users.models import Users


class News(TimeStamp):
    news_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE,
        verbose_name="Название новости",
    )
    news_image = models.ImageField(
        upload_to="images/news/", verbose_name="Фотография к новости"
    )
    news_text = models.TextField(verbose_name="Описание новости")
    news_regional_divisions = models.ManyToManyField(
        RegionalDivisions, verbose_name="Региональные отделения", related_name="news"
    )
    news_disciplines = models.ManyToManyField(
        Disciplines, verbose_name="Дисциплины", related_name="news"
    )
    event_city = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Город",
        related_name="news",
    )
    news_author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Автор новости",
        related_name="news_author",
    )
    news_reading_time = models.IntegerField(
        default=5,
        verbose_name="Время на чтение (в минутах)",
    )

    def __str__(self):
        return self.news_title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
