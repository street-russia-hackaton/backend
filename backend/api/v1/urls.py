from api.v1.users.views import UserPassportViewSet, UsersViewSet
from api.v1.views import (
    CitiesViewSet,
    DisciplinesViewSet,
    DonatsViewSet,
    EventsViewSet,
    NewsViewSet,
    ObjectSportViewSet,
    PartnersViewSet,
    RegionalDivisionsViewSet,
    RegionsViewSet,
)
from django.urls import include, path
from rest_framework import routers

app_name = "api.v1"


router = routers.DefaultRouter()

router.register("users", UsersViewSet, "users")
router.register("regions", RegionsViewSet, basename="region")
router.register("cities", CitiesViewSet, basename="city")
router.register("passports", UserPassportViewSet, basename="passport")
router.register("events", EventsViewSet, basename="event")
router.register("disciplines", DisciplinesViewSet, basename="discipline")
router.register("partners", PartnersViewSet, basename="partner")
router.register("object_sports", ObjectSportViewSet, basename="object_sport")
router.register(
    "regional_divisions", RegionalDivisionsViewSet, basename="regional_division"
)
router.register("news", NewsViewSet, basename="new")
router.register("donats", DonatsViewSet, basename="donat")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
