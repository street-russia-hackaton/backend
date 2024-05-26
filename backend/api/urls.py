from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import (
    RegionsViewSet,
    CitiesViewSet,
    UsersViewSet,
    EventsViewSet,
    DisciplinesViewSet,
    PartnersViewSet,
    ObjectSportViewSet,
    RegionalDivisionsViewSet,
    NewsViewSet,
    UserPassportViewSet,
)

app_name = "api"

router = DefaultRouter()
router.register("regions", RegionsViewSet, basename="region")
router.register("cities", CitiesViewSet, basename="city")
router.register("users", UsersViewSet, basename="user")
router.register("passports", UserPassportViewSet, basename="passport")
router.register("events", EventsViewSet, basename="event")
router.register("disciplines", DisciplinesViewSet, basename="discipline")
router.register("partners", PartnersViewSet, basename="partner")
router.register("object_sports", ObjectSportViewSet, basename="object_sport")
router.register("regional_divisions", RegionalDivisionsViewSet, basename="regional_division")
router.register("news", NewsViewSet, basename="new")


urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
