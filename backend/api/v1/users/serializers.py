from djoser.serializers import UserCreateSerializer, UserSerializer
from drf_base64.fields import Base64ImageField
from rest_framework import serializers
from users.models import UserPassport, Users


class UsersCreateSerializer(UserCreateSerializer):
    """
    Сериализатор для создания нового пользователя.
    """

    photo = Base64ImageField()

    class Meta:
        model = Users
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "photo",
            "phone",
            "birth_year",
            "position",
            "account_status",
            "career_start",
            "biography",
            "vk_link",
            "video_profile",
        )
        extra_kwargs = {
            "username": {"required": True},
            "email": {"required": True},
            "password": {"write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "middle_name": {"required": True},
            "phone": {"required": True},
            "birth_year": {"required": True},
        }


class UserPassportSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения доп. информации о пользователях.
    """

    class Meta:
        model = UserPassport
        fields = (
            "id",
            "passport_series",
            "passport_number",
            "passport_issued_by",
            "passport_issued_at",
            "accept_rules",
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.save()
        return instance


class UsersSerializer(UserSerializer):
    """
    Сериализатор для чтения информации о пользователе.
    """

    photo = Base64ImageField()
    passport = UserPassportSerializer()

    class Meta:
        model = Users
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "phone",
            "photo",
            "birth_year",
            "position",
            "account_status",
            "career_start",
            "biography",
            "vk_link",
            "video_profile",
            "passport",
        )
