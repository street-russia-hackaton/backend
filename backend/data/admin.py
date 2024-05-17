from django.contrib import admin

from .models import Cities, Regions, ObjectSport, ObjectSportImage, Disciplines, Partners


class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city_title',)
    list_filter = ('city_title',)


class RegionsAdmin(admin.ModelAdmin):
    list_display = ('region_title',)
    list_filter = ('region_title',)


class ObjectSportAdmin(admin.ModelAdmin):
    list_display = ('object_sport_title', 'object_sport_indoor_outdoor', 'object_sport_address')
    list_filter = ('object_sport_indoor_outdoor',)


class ObjectSportImageAdmin(admin.ModelAdmin):
    list_display = ('object_sport_image',)
    list_filter = ('object_sport_image',)


class DisciplinesAdmin(admin.ModelAdmin):
    list_display = ('disciplines_title', 'disciplines_video_url',)
    list_filter = ('disciplines_information',)


class PartnersAdmin(admin.ModelAdmin):
    list_display = ('partners_title', 'partners_category',)
    list_filter = ('partners_category',)


admin.site.register(ObjectSportImage, ObjectSportImageAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(Regions, RegionsAdmin)
admin.site.register(ObjectSport, ObjectSportAdmin)
admin.site.register(Disciplines, DisciplinesAdmin)
admin.site.register(Partners, PartnersAdmin)
