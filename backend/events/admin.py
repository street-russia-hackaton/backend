from django.contrib import admin
from events.models import Events, FavoriteEvents, RegisteredEvents


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ("event_title", "event_start_date", "event_city", "event_curator")
    list_filter = ("event_city", "event_curator")


@admin.register(FavoriteEvents)
class FavoriteEventsAdmin(admin.ModelAdmin):
    list_display = ("user", "event")
    list_filter = ("user", "event")


@admin.register(RegisteredEvents)
class RegisteredEventsAdmin(admin.ModelAdmin):
    list_display = ("user", "event")
    list_filter = ("user", "event")
