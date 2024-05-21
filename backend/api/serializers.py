from rest_framework import serializers
from data.models import(
    Regions,
    Cities
) 
from events.models import(
    Events,
    FavoriteEvents,
    RegisteredEvents
)
from info.models import(
    Disciplines,
    Partners,
    ObjectSport,
    ObjectSportImage,
    RegionalDivisions
)
from news.models import(
    News
)
from news.models import(
    TimeStamp
)
from users.models import(
    Users,
    UserPassport
)


class CitiesSerializer(serializers.ModelSerializer):
    """Сериализатор для городов."""

    city_region = serializers.SlugRelatedField(slug_field='region_title', queryset=Regions.objects.all())

    class Meta:
        model = Cities
        fields = ("id", "city_title", "city_region")


class RegionsSerializer(serializers.ModelSerializer):
    """Сериализатор для регионов."""

    class Meta:
        model = Regions
        fields = ("id", "region_title")


class EventsSerializer(serializers.ModelSerializer):
    """Сериализатор для мероприятий."""
    class Meta:
        model = Events
        fields = '__all__'

class FavoriteEventsSerializer(serializers.ModelSerializer):
    """Сериализатор для избранных мероприятий."""
    class Meta:
        model = FavoriteEvents
        fields = ('user', 'event')

class RegisteredEventsSerializer(serializers.ModelSerializer):
    """Сериализатор для зарегистрированных на мероприятие."""
    class Meta:
        model = RegisteredEvents
        fields = ('user', 'event')

class DisciplinesSerializer(serializers.ModelSerializer):
    """Сериализатор для дисциплин."""
    class Meta:
        model = Disciplines
        fields = '__all__'

class PartnersSerializer(serializers.ModelSerializer):
    """Сериализатор для партнеров."""
    class Meta:
        model = Partners
        fields = '__all__'

class ObjectSportSerializer(serializers.ModelSerializer):
    """Сериализатор для спортивных объектов."""
    class Meta:
        model = ObjectSport
        fields = '__all__'

class ObjectSportImageSerializer(serializers.ModelSerializer):
    """Сериализатор для изображений спортивных объектов."""
    class Meta:
        model = ObjectSportImage
        fields = '__all__'

class RegionalDivisionsSerializer(serializers.ModelSerializer):
    """Сериализатор для региональных подразделений."""
    class Meta:
        model = RegionalDivisions
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор для новостей."""
    class Meta:
        model = News
        fields = '__all__'

class TimeStampSerializer(serializers.ModelSerializer):
    """Сериализатор для временных меток."""
    class Meta:
        model = TimeStamp
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей."""
    class Meta:
        model = Users
        fields = '__all__'

class UserPassportSerializer(serializers.ModelSerializer):
    """Сериализатор для паспортных данных пользователей."""
    class Meta:
        model = UserPassport
        fields = '__all__'

