from rest_framework import viewsets

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

from .serializers import (
    RegionsSerializer,
    CitiesSerializer,
    EventsSerializer, 
    FavoriteEventsSerializer,
    RegisteredEventsSerializer, 
    DisciplinesSerializer,
    PartnersSerializer,
    ObjectSportSerializer, 
    RegionalDivisionsSerializer,
    NewsSerializer,
    ObjectSportImageSerializer,
    UsersSerializer,
    UserPassportSerializer
)

class RegionsViewSet(viewsets.ModelViewSet):
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer

class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class FavoriteEventsViewSet(viewsets.ModelViewSet):
    queryset = FavoriteEvents.objects.all()
    serializer_class = FavoriteEventsSerializer

class RegisteredEventsViewSet(viewsets.ModelViewSet):
    queryset = RegisteredEvents.objects.all()
    serializer_class = RegisteredEventsSerializer

class DisciplinesViewSet(viewsets.ModelViewSet):
    queryset = Disciplines.objects.all()
    serializer_class = DisciplinesSerializer

class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class ObjectSportViewSet(viewsets.ModelViewSet):
    queryset = ObjectSport.objects.all()
    serializer_class = ObjectSportSerializer

class RegionalDivisionsViewSet(viewsets.ModelViewSet):
    queryset = RegionalDivisions.objects.all()
    serializer_class = RegionalDivisionsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UserPassportViewSet(viewsets.ModelViewSet):
    queryset = UserPassport.objects.all()
    serializer_class = UserPassportSerializer
