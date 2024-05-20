from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import UserPassport, Users


@receiver(post_save, sender=Users)
def create_or_update_user_passport(sender, instance, created, **kwargs):
    if created:
        # Если пользователь только что создан, создаем для него паспортные данные
        UserPassport.objects.create(user=instance)
