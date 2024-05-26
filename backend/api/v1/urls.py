from api.v1.users.views import UsersViewSet
from django.urls import include, path
from rest_framework import routers

app_name = "api.v1"


router = routers.DefaultRouter()

router.register("users", UsersViewSet, "users")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
