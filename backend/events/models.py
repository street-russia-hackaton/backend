from datetime import datetime
from io import BytesIO

import qrcode
from core.constants import FieldLength
from data.models import Cities
from django.core.files import File
from django.db import models
from info.models import Disciplines, Partners, RegionalDivisions
from users.models import Users


class Events(models.Model):
    event_title = models.CharField(
        max_length=FieldLength.MAX_LENGTH_TITLE, verbose_name="Название мероприятия"
    )
    event_image = models.ImageField(
        upload_to="images/events/", verbose_name="Изображение мероприятия"
    )
    event_start_date = models.DateTimeField(
        default=datetime.now, verbose_name="Дата начала мероприятия"
    )
    event_end_date = models.DateTimeField(
        default=datetime.now, verbose_name="Дата окончания мероприятия"
    )
    event_information = models.TextField(verbose_name="Информация о мероприятии")
    event_disciplines = models.ManyToManyField(
        Disciplines,
        verbose_name="Дисциплины",
    )
    event_regional_division = models.ForeignKey(
        RegionalDivisions,
        on_delete=models.CASCADE,
        verbose_name="Региональное отделение",
        related_name="events_regional_division",
    )
    event_city = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
        verbose_name="Город",
        related_name="events_city",
    )
    event_curator = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Организатор мероприятия",
        related_name="events_curator",
    )
    event_partner = models.ManyToManyField(
        Partners,
        verbose_name="Партнеры мероприятия",
    )
    event_qr_code = models.ImageField(
        upload_to="images/events/qr_codes/",
        blank=True,
        null=True,
        verbose_name="QR-код",
    )
    event_ics_file = models.FileField(
        upload_to="images/events/ics_files/",
        blank=True,
        null=True,
        verbose_name="Файл календаря",
    )
    event_is_pets = models.BooleanField(
        "Можно с животными",
        default=False,
    )
    event_is_food = models.BooleanField(
        "Можно ли со своей едой",
        default=False,
    )
    event_is_wc = models.BooleanField(
        "Есть ли туалет",
        default=False,
    )
    event_is_disabled = models.BooleanField(
        "Для людей с ограниченными возможностями",
        default=False,
    )

    def generate_calendar_link(self):
        # Формирование данных для QR-кода/файла
        qr_meta_start = "BEGIN:VCALENDAR\nBEGIN:VEVENT\n"
        qr_meta_end = "END:VEVENT\nEND:VCALENDAR"
        cal_start_time = self.event_start_date.strftime("%Y%m%dT%H%M%S")
        cal_end_time = self.event_end_date.strftime("%Y%m%dT%H%M%S")
        qr_data_info = (
            f"SUMMARY:{self.event_title}\n"
            f"DESCRIPTION:{self.event_information}\n"
            f"LOCATION:{self.event_city}\n"
        )
        qr_data_dates = f"DTSTART:{cal_start_time}\nDTEND:{cal_end_time}\n"
        print(qr_data_dates)

        # Создание объекта QR-кода
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_data = qr_meta_start + qr_data_info + qr_data_dates + qr_meta_end
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Создание изображения QR-кода
        img = qr.make_image(fill_color="black", back_color="white")

        # Сохранение изображения в байтовый объект
        qr_buffer = BytesIO()
        img.save(qr_buffer, format="PNG")

        # Сохранение данных в байтовый объект
        ics_buffer = BytesIO()
        ics_buffer.write(qr_data.encode("utf-8"))
        ics_buffer.seek(0)

        # Сохранение изображения как поля модели
        self.event_qr_code.save(f"qr_code_{self.pk}.png", File(qr_buffer), save=False)
        # Сохранение данных о событии как поля модели
        self.event_ics_file.save(f"ics_{self.pk}.ics", File(ics_buffer), save=False)

    def save(self, *args, **kwargs):
        # Генерирование создания события в календаре при сохранении объекта модели
        self.generate_calendar_link()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.event_title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class FavoriteEvents(models.Model):
    """Модель добавления мероприятия в избранное"""

    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="участник",
        related_name="participants_favorite",
    )
    event = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        verbose_name="мероприятие",
        related_name="event_favorite",
    )

    class Meta:
        verbose_name = "Избранное мероприятие"
        verbose_name_plural = "Избранные мероприятия"
        constraints = [
            models.UniqueConstraint(fields=["user", "event"], name="user_event")
        ]

    def __str__(self):
        return f"{self.user} - {self.event}"


class RegisteredEvents(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="participant_registered",
    )
    event = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        verbose_name="Мероприятие",
        related_name="event_registered",
    )

    def __str__(self):
        return f"{self.user} - {self.event}"

    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрации"
        constraints = [
            models.UniqueConstraint(fields=["event", "user"], name="event_user")
        ]
