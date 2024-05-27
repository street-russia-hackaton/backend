from data.models import Cities, Regions
from drf_base64.fields import Base64ImageField
from events.models import Events, FavoriteEvents, RegisteredEvents
from info.models import (
    Disciplines,
    Donats,
    ObjectSport,
    ObjectSportImage,
    Partners,
    RegionalDivisions,
)
from news.models import News, TimeStamp
from rest_framework import serializers
from users.models import UserPassport, Users


class RegionalDivisionsCuratorSerializer(serializers.ModelSerializer):
    """Сериализатор для куратора регионального отделения."""

    photo = Base64ImageField()

    class Meta:
        model = Users
        fields = (
            "last_name",
            "first_name",
            "photo",
            "position",
            "vk_link",
        )


class RegionalDivisionsPartnersSerializer(serializers.ModelSerializer):
    """Сериализатор для партнеров региональных отделений."""

    class Meta:
        model = Partners
        fields = ("partners_title", "partners_logo")


class RegionalDivisionsShortSerializer(serializers.ModelSerializer):
    """Сериализатор для региональных отделений на главной странице на карте."""

    sport_objects_count = serializers.SerializerMethodField()
    events_count = serializers.SerializerMethodField()
    cities_list = serializers.SerializerMethodField()

    class Meta:
        model = RegionalDivisions
        fields = (
            "id",
            "regional_divisions_title",
            "sport_objects_count",
            "events_count",
            "cities_list",
        )

    def get_sport_objects_count(self, obj):
        """Метод для подсчета количества спортивных объектов у регионального отделения."""
        return obj.regional_divisions_sport_obj.count()

    def get_events_count(self, obj):
        """Метод для подсчета количества мероприятий, связанных с региональным отделением."""
        return obj.events_set.count()

    def get_cities_list(self, obj):
        """Метод для вывода списка городов, связанных с региональным отделением (до 3 штук)."""
        cities = obj.regional_divisions_сity.all()[:3]
        return [city.city_name for city in cities]


class RegionalDivisionsFullSerializer(serializers.ModelSerializer):
    """Сериализатор для региональных подразделений подробнее."""

    regional_divisions_curator = RegionalDivisionsCuratorSerializer()
    regional_divisions_partner = RegionalDivisionsPartnersSerializer()

    class Meta:
        model = RegionalDivisions
        fields = (
            "regional_divisions_title",
            "regional_divisions_image",
            "regional_divisions_information",
            "regional_divisions_curator",
            "regional_divisions_partner",
        )


class RegionalDivisionsListSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализатор для региональных подразделений список по регионам в алфавитном порядке."""

    class Meta:
        model = RegionalDivisions
        fields = ("url", "regional_divisions_region")
        extra_kwargs = {
            "url": {"view_name": "regionaldivision-detail", "lookup_field": "id"}
        }


class EventsShotSerializer(serializers.ModelSerializer):
    """Cериализатор для мероприятий на главной странице."""

    event_city = serializers.SlugRelatedField(
        slug_field="city_title", queryset=Cities.objects.all(), label="Город"
    )
    event_disciplines = serializers.SlugRelatedField(
        slug_field="disciplines_title",
        queryset=Disciplines.objects.all(),
        label="Название дисциплины",
    )

    class Meta:
        model = Events
        fields = (
            "event_image",
            "event_title",
            "event_information",
            "event_city",
            "event_disciplines",
            "event_start_date",
            "event_end_date",
        )


class EventsFullSerializer(serializers.ModelSerializer):
    """Cериализатор для мероприятий подробнее."""

    class Meta:
        model = UserPassport
        fields = "__all__"


class DisciplinesSerializer(serializers.ModelSerializer):
    """Сериализатор для дисциплин."""

    class Meta:
        model = Disciplines
        fields = (
            "id",
            "disciplines_title",
            "disciplines_image",
            "disciplines_information",
            "disciplines_video_url",
        )


class NewsSerializer(serializers.ModelSerializer):
    """Короткий сериализатор для новостей на главной странице."""

    news_disciplines = serializers.SlugRelatedField(
        slug_field="disciplines_title",
        queryset=Disciplines.objects.all(),
        many=True,
        label="Дисциплины",
    )

    class Meta:
        model = News
        fields = (
            "id",
            "news_title",
            "news_image",
            "news_text",
            "news_disciplines",
            "news_reading_time",
        )


class CitiesSerializer(serializers.ModelSerializer):
    """Сериализатор для городов."""

    city_region = serializers.SlugRelatedField(
        slug_field="region_title", queryset=Regions.objects.all(), label="Регион"
    )

    class Meta:
        model = Cities
        fields = ("id", "city_title", "city_region")


class RegionsSerializer(serializers.ModelSerializer):
    """Сериализатор для регионов."""

    class Meta:
        model = Regions
        fields = ("id", "region_title")


class FavoriteEventsSerializer(serializers.ModelSerializer):
    """Сериализатор для избранных мероприятий."""

    class Meta:
        model = FavoriteEvents
        fields = ("user", "event")


class RegisteredEventsSerializer(serializers.ModelSerializer):
    """Сериализатор для зарегистрированных на мероприятие."""

    class Meta:
        model = RegisteredEvents
        fields = ("user", "event")


class PartnersSerializer(serializers.ModelSerializer):
    """Сериализатор для партнеров."""

    class Meta:
        model = Partners
        fields = "__all__"


class ObjectSportSerializer(serializers.ModelSerializer):
    """Сериализатор для спортивных объектов."""

    class Meta:
        model = ObjectSport
        fields = "__all__"


class ObjectSportImageSerializer(serializers.ModelSerializer):
    """Сериализатор для изображений спортивных объектов."""

    class Meta:
        model = ObjectSportImage
        fields = "__all__"


class DonatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donats
        fields = "__all__"


class TimeStampSerializer(serializers.ModelSerializer):
    """Сериализатор для временных меток."""

    class Meta:
        model = TimeStamp
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей."""

    class Meta:
        model = Users
        fields = "__all__"
