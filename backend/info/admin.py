from django.contrib import admin

from .models import RegionalDivisions
from .models import News, FollowersNews
from .models import Events, FavoriteEvents, RegisteredEvents


class RegionalDivisionsAdmin(admin.ModelAdmin):
    list_display = ('regional_divisions_title', 'regional_divisions_regions',)
    list_filter = ('regional_divisions_regions',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_date',)
    list_filter = ('regional_divisions', 'disciplines', 'autors',)


class EventsAdmin(admin.ModelAdmin):
    list_display = ('events_title', 'events_date', 'events_city', 'events_curator')
    list_filter = ('events_city', 'events_curator')


class FavoriteEventsAdmin(admin.ModelAdmin):
    list_display = ('user', 'events')
    list_filter = ('user', 'events')


class RegisteredEventsAdmin(admin.ModelAdmin):
    list_display = ('user', 'events')
    list_filter = ('user', 'events')


class FollowersNewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'news',)
    list_filter = ('user', 'news',)


admin.site.register(FollowersNews, FollowersNewsAdmin)
admin.site.register(RegionalDivisions, RegionalDivisionsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(RegisteredEvents, RegisteredEventsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(FavoriteEvents, FavoriteEventsAdmin)
