from django.db import models


class TimeStamp(models.Model):
    """Модель временных меток"""

    created_at = models.DateTimeField("дата создания", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("дата обновления", auto_now=True, db_index=True)

    class Meta:
        abstract = True
