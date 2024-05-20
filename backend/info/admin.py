from django.contrib import admin

from .models import (
    Disciplines,
    ObjectSport,
    ObjectSportImage,
    Partners,
    RegionalDivisions,
)


@admin.register(ObjectSport)
class ObjectSportAdmin(admin.ModelAdmin):
    list_display = ("object_sport_title", "object_sport_type", "object_sport_address")
    list_filter = ("object_sport_type",)


@admin.register(ObjectSportImage)
class ObjectSportImageAdmin(admin.ModelAdmin):
    list_display = ("object_sport_image",)
    list_filter = ("object_sport_image",)


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = (
        "partners_title",
        "partners_category",
    )
    list_filter = ("partners_category",)


@admin.register(RegionalDivisions)
class RegionalDivisionsAdmin(admin.ModelAdmin):
    list_display = (
        "regional_divisions_title",
        "regional_divisions_region",
    )
    list_filter = ("regional_divisions_region",)


@admin.register(Disciplines)
class DisciplinesAdmin(admin.ModelAdmin):
    list_display = (
        "disciplines_title",
        "disciplines_video_url",
    )
    list_filter = ("disciplines_title",)
