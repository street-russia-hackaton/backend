from django.db import models


class PartnerRoleChoices(models.TextChoices):
    """Ранжирование партнеров."""

    STRATEGIC = ("strategic", "Стратегические партнеры")
    ORGANIZATIONAL = ("organizational", "Организационные партнеры")
    REGIONAL = ("regional", "Региональные партнеры")
    GENERAL = ("general", "Генеральные партнеры")


class ObjectTypeChoices(models.TextChoices):
    """Тип спортивного объекта"""

    OUTDOOR = ("outdoor", "Открытое")
    INDOOR = ("indoor", "Закрытое")
