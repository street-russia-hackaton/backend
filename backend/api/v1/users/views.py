from api.v1.users.permissions import IsOwnerOrAdminOrReadOnly
from api.v1.users.serializers import (
    UserPassportSerializer,
    UsersCreateSerializer,
    UsersSerializer,
)
from djoser.views import UserViewSet
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from users.models import UserPassport, Users


class UsersViewSet(UserViewSet):
    """
    Представление для получения информации о пользователях.
    """

    queryset = Users.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Выбор сериализатора в зависимости от
        просмотра или создания пользователя.
        """
        if self.request.method in SAFE_METHODS:
            return UsersSerializer
        return UsersCreateSerializer


class UserPassportViewSet(ModelViewSet):
    """
    Представление для получения доп. информации о пользователях.
    """

    queryset = UserPassport.objects.all()
    serializer_class = UserPassportSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
