from api.v1.paginations import (
    DisciplinesPagination,
    EventsShotPagination,
    NewsPagination,
)
from data.models import Cities, Regions
from events.models import Events, FavoriteEvents, RegisteredEvents
from info.models import Disciplines, Donats, ObjectSport, Partners, RegionalDivisions
from news.models import News
from rest_framework import viewsets

from .serializers import (
    CitiesSerializer,
    DisciplinesSerializer,
    DonatsSerializer,
    EventsFullSerializer,
    EventsShotSerializer,
    FavoriteEventsSerializer,
    NewsSerializer,
    ObjectSportSerializer,
    PartnersSerializer,
    RegionalDivisionsFullSerializer,
    RegionalDivisionsShortSerializer,
    RegionsSerializer,
    RegisteredEventsSerializer,
)


class RegionsViewSet(viewsets.ModelViewSet):
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class EventsViewSet(viewsets.ModelViewSet):
    pagination_class = EventsShotPagination
    queryset = Events.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return EventsShotSerializer
        return EventsFullSerializer


class FavoriteEventsViewSet(viewsets.ModelViewSet):
    queryset = FavoriteEvents.objects.all()
    serializer_class = FavoriteEventsSerializer


class RegisteredEventsViewSet(viewsets.ModelViewSet):
    queryset = RegisteredEvents.objects.all()
    serializer_class = RegisteredEventsSerializer


class DisciplinesViewSet(viewsets.ModelViewSet):
    queryset = Disciplines.objects.all()
    serializer_class = DisciplinesSerializer
    pagination_class = DisciplinesPagination


class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer


class ObjectSportViewSet(viewsets.ModelViewSet):
    queryset = ObjectSport.objects.all()
    serializer_class = ObjectSportSerializer


class RegionalDivisionsViewSet(viewsets.ModelViewSet):
    queryset = RegionalDivisions.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return RegionalDivisionsShortSerializer
        return RegionalDivisionsFullSerializer


class DonatsViewSet(viewsets.ModelViewSet):
    queryset = Donats.objects.all()
    serializer_class = DonatsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    pagination_class = NewsPagination
    serializer_class = NewsSerializer
