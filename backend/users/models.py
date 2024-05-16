from django.db import models
from django.core.validators import RegexValidator


class Users(models.Model):
    USER = 'user'
    MEMBER = 'member'
    CURATOR = 'curator'
    REGIONAL_LEADER = 'regional_leader'
    CENTRAL_LEADERSHIP = 'central_leadership'
    
    ACCOUNT_STATUS_CHOICES = [
        (USER, 'Пользователь'),
        (MEMBER, 'Участник'),
        (CURATOR, 'Куратор'),
        (REGIONAL_LEADER, 'Региональный руководитель'),
        (CENTRAL_LEADERSHIP, 'Центральное руководство'),
    ]
    
    username = models.CharField(
        max_length=100,
        verbose_name="Логин"
    )
    password = models.CharField(
        max_length=100,
        verbose_name="Пароль"
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия"
    )
    middle_name = models.CharField(
        max_length=100,
        verbose_name="Отчество"
    )
    email = models.EmailField(
        verbose_name="Электронная почта"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон"
    )
    position = models.CharField(
        max_length=100,
        verbose_name="Должность"
    )
    account_status = models.CharField(
        max_length=20,
        choices=ACCOUNT_STATUS_CHOICES,
        default=USER,
        verbose_name="Статус аккаунта"
    )
    birth_year = models.DateField(
        verbose_name="Дата рождения"
    )
    career_start = models.DateField(
        verbose_name="Дата начала карьеры"
    )
    biography = models.TextField(
        verbose_name="Биография"
    )
    passport_series = models.IntegerField(
        validators=[RegexValidator(
            r'^\d{1,10}$', message='Only digits are allowed'
        )],
        verbose_name="Серия паспорта"
    )
    passport_number = models.IntegerField(
        validators=[RegexValidator(
            r'^\d{1,20}$', message='Only digits are allowed'
        )],
        verbose_name="Номер паспорта"
    )
    passport_issued_by = models.CharField(
        max_length=100,
        verbose_name="Кем выдан паспорт"
    )
    vk_link = models.URLField(
        verbose_name="Ссылка на ВК"
    )
    video_profile = models.FileField(
        upload_to='video_profiles/',
        verbose_name="Видеовизитка"
    )

    def __str__(self):
            return f"{self.last_name} {self.first_name} {self.middle_name}"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
