from datetime import date

from core.constants import UserFieldsLength
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models

from .choice_classes import RoleChoices
from .validators import validate_username


class Users(AbstractUser):
    username = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_USERNAME,
        verbose_name="Логин",
        unique=True,
        validators=(validate_username, UnicodeUsernameValidator()),
    )
    password = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_PASSWORD, verbose_name="Пароль"
    )
    first_name = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_FIRST_NAME, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_LAST_NAME, verbose_name="Фамилия"
    )
    middle_name = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_MIDDLE_NAME, verbose_name="Отчество"
    )
    email = models.EmailField(
        max_length=UserFieldsLength.MAX_LENGTH_EMAIL,
        verbose_name="Электронная почта",
        unique=True,
    )
    phone = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_PHONE,
        verbose_name="Телефон",
        unique=True,
    )
    photo = models.ImageField(
        "Фото",
        upload_to="users/images/",
        null=True,
        default=None,
        blank=True,
    )
    position = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_POSITION,
        verbose_name="Должность",
        blank=True,
    )
    account_status = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_STATUS,
        choices=RoleChoices,
        default=RoleChoices.USER,
        verbose_name="Статус аккаунта",
    )
    birth_year = models.DateField(verbose_name="Дата рождения", default=date.today)
    career_start = models.DateField(
        verbose_name="Дата начала карьеры", blank=True, null=True
    )
    biography = models.TextField(verbose_name="Биография", blank=True)
    vk_link = models.URLField(verbose_name="Ссылка на ВК", blank=True)
    video_profile = models.FileField(
        upload_to="video_profiles/", verbose_name="Видеовизитка", blank=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone", "email"]

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserPassport(models.Model):
    """
    Модель для паспортных данных пользователя.
    """

    user = models.OneToOneField(
        Users,
        on_delete=models.CASCADE,
        related_name="passport",
        verbose_name="Пользователь",
    )
    passport_series = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_SERIES,
        validators=[RegexValidator(r"^\d{1,10}$", message="Only digits are allowed")],
        verbose_name="Серия паспорта",
        default="",
    )
    passport_number = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_NUMBER,
        validators=[RegexValidator(r"^\d{1,20}$", message="Only digits are allowed")],
        verbose_name="Номер паспорта",
        default="",
    )
    passport_issued_by = models.CharField(
        max_length=UserFieldsLength.MAX_LENGTH_ISSUED,
        verbose_name="Кем выдан паспорт",
        default="",
    )
    passport_issued_at = models.DateField(
        verbose_name="Дата выдачи", default=date.today
    )
    accept_rules = models.BooleanField(
        "Cогласие с правами и обязанностями участника",
        default=False,
    )

    class Meta:
        verbose_name = "Инфо о паспорте пользователя"
        verbose_name_plural = "Инфо о паспортах пользователей"
        ordering = ["-pk"]

    def __str__(self):
        return str(self.pk)
