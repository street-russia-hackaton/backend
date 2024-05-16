from django.db import models
from datetime import date

from data.models import Cities, Regions, Disciplines
from users.models import Users


class Events(models.Model):
    events_title = models.CharField(
        max_length=100,
        verbose_name="Название мероприятия"
    )
    events_image = models.ImageField(
        upload_to='images/events/',
        verbose_name="Изображение мероприятия"
    )
    events_date = models.DateField(
        default=date.today,
        verbose_name="Дата мероприятия"
    )
    events_information = models.TextField(
        verbose_name="Информация о мероприятии"
    )
    events_disciplines = models.ForeignKey(
        Disciplines,
        on_delete=models.CASCADE,
        verbose_name="Дисциплины"
    )
    events_city = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
        verbose_name="Город"
    )
    events_curator = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Организатор мероприятия"
    )

    def __str__(self):
        return self.events_title
    
    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class FavoriteEvents(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    events = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        verbose_name="Мероприятие"
    )

    def __str__(self):
        return f"{self.user} - {self.events}"
    
    class Meta:
        verbose_name = "Избранное мероприятие"
        verbose_name_plural = "Избранные мероприятия"


class RegisteredEvents(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    events = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        verbose_name="Мероприятие"
    )

    def __str__(self):
        return f"{self.user} - {self.events}"

    class Meta:
        verbose_name = "Зарегистрированный пользователь на мероприятие"
        verbose_name_plural = "Зарегистрированные пользователи на мероприятия"


class RegionalDivisions(models.Model):
    regional_divisions_title = models.CharField(
        max_length=100,
        verbose_name="Название регионального отделения"
    )
    regional_divisions_image = models.ImageField(
        upload_to='images/regional_divisions/',
        verbose_name="Фотографии региональных отделений"
    )
    regional_divisions_information = models.TextField(
        verbose_name="Общая информация регионального отделения"
    )
    regional_divisions_info = models.TextField(
        verbose_name="Описание регионального отделения"
    )
    regional_divisions_сities = models.ManyToManyField(
        Cities,
        verbose_name="Список городов"
    )
    regional_divisions_regions = models.OneToOneField(
        Regions,
        on_delete=models.CASCADE,
        verbose_name="Регион"
    )
    regional_divisions_disciplines = models.ManyToManyField(
        Disciplines,
        verbose_name="Дисциплина"
    )
    regional_divisions_events = models.ManyToManyField(
        Events,
        verbose_name="Мероприятия в данном регионе"
    )
    regional_divisions_curators = models.ForeignKey(
        Users,
         on_delete=models.CASCADE,
        verbose_name="Руководитель регионального отделения"
    )

    def __str__(self):
        return self.regional_divisions_title

    class Meta:
        verbose_name = "Региональное отделение"
        verbose_name_plural = "Региональные отделения"


class News(models.Model):
    news_title = models.CharField(
        max_length=100,
        verbose_name="Название новости"
    )
    news_image = models.ImageField(
        upload_to='images/news/',
        verbose_name="Фотография"
    )
    news_date = models.DateField(
        verbose_name="Дата"
    )
    news_text = models.TextField(
        verbose_name="Описание новости"
    )
    regional_divisions = models.ManyToManyField(
        RegionalDivisions,
        verbose_name="Региональные отделения"
    )
    disciplines = models.ManyToManyField(
        Disciplines,
        verbose_name="Дисциплины"
    )
    autors = models.ManyToManyField(
        Users,
        verbose_name="Авторы"
    )

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class FollowersNews(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name="Новости"
    )

    def __str__(self):
        return f"{self.user} - {self.news}"

    class Meta:
        verbose_name = "Подписчик на новость"
        verbose_name_plural = "Подписчики на новость"
