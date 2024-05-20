from core.constants import FieldLength
from core.models import TimeStamp
from data.models import Disciplines
from django.db import models
from info.models import RegionalDivisions
from users.models import Users


class News(TimeStamp):
    news_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE,
        verbose_name="Название новости",
    )
    news_image = models.ImageField(upload_to="images/news/", verbose_name="Фотография")
    news_text = models.TextField(verbose_name="Описание новости")
    news_regional_divisions = models.ManyToManyField(
        RegionalDivisions, verbose_name="Региональные отделения", related_name="news"
    )
    news_disciplines = models.ManyToManyField(
        Disciplines, verbose_name="Дисциплины", related_name="news"
    )
    news_author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Автор новости",
        related_name="news_author",
    )

    def __str__(self):
        return self.news_title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
