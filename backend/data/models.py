from django.db import models


class Cities(models.Model):
    city_title = models.CharField(
        max_length=100,
        verbose_name="Название города"
    )

    def __str__(self):
        return self.city_title

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Regions(models.Model):
    region_title = models.CharField(
        max_length=100,
        verbose_name="Название региона"
    )

    def __str__(self):
        return self.region_title

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Disciplines(models.Model):
    disciplines_title = models.CharField(
        max_length=100,
        verbose_name="Название дисциплины"
    )
    disciplines_image = models.ImageField(
        upload_to='images/disciplines/',
        verbose_name="Фотография дисциплины"
    )
    disciplines_video_url = models.URLField(
        verbose_name="Ссылка на видео"
    )
    disciplines_information = models.TextField(
        verbose_name="Информация о дисциплине"
    )

    def __str__(self):
        return self.disciplines_title
    
    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
    

class Partners(models.Model):
    STRATEGIC = 'strategic'
    ORGANIZATIONAL = 'organizational'
    REGIONAL = 'regional'
    GENERAL = 'general' 

    CATEGORY_CHOICES = [
        (STRATEGIC, 'Стратегические партнеры'),
        (ORGANIZATIONAL, 'Организационные партнеры'),
        (REGIONAL, 'Региональные партнеры'),
        (GENERAL, 'Генеральные партнеры'), 
    ]

    partners_title = models.CharField(
        max_length=100,
        verbose_name="Название партнера"
    )
    partners_category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default=STRATEGIC,
        verbose_name="Категория партнера"
    )
    partners_logo = models.ImageField(
        upload_to='images/partners/',
        verbose_name="Логотип партнера"
    )
    partners_url = models.URLField(
        verbose_name="Ссылка на сайт партнера"
    )

    def __str__(self):
        return self.partners_title
    
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class ObjectSportImage(models.Model):
    object_sport_image = models.ImageField(
        upload_to='images/object_sport/',
        verbose_name="Фотография спортивного обьекта"
    )

    def __str__(self):
        return str(self.object_sport_image)

    class Meta:
            verbose_name = "Фотография спортивного обьекта"
            verbose_name_plural = "Фотография спортивных обьектов"


class ObjectSport(models.Model):
    object_sport_title = models.CharField(
        max_length=100,
        verbose_name="Название спортивного объекта"
    )
    object_sport_image = models.ManyToManyField(
        ObjectSportImage,
        verbose_name="Фотография спортивного обьекта"
    )
    object_sport_video = models.URLField(
        verbose_name="Ссылка на видео объекта спорта"
    )
    object_sport_indoor_outdoor = models.CharField(
        max_length=10,
        verbose_name="Помещение (закрытое/открытое)"
    )
    object_sport_info = models.CharField(
        max_length=100,
        verbose_name="Описание объекта"
    )
    object_sport_address = models.CharField(
        max_length=100,
        verbose_name="Адрес обьекта"
    )

    def __str__(self):
        return self.object_sport_title

    class Meta:
        verbose_name = "Спортивный объект"
        verbose_name_plural = "Спортивные объекты"
            