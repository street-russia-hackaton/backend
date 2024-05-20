from django.db import models


class RoleChoices(models.TextChoices):
    """Определение роли юзера."""

    USER = ("user", "Пользователь")
    MEMBER = ("member", "Участник")
    CURATOR = ("curator", "Куратор")
    REGIONAL_LEADER = ("regional_leader", "Региональный руководитель")
    CENTRAL_LEADERSHIP = ("central_leadership", "Центральное руководство")
