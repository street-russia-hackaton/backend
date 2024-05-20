from django.contrib import admin

from .models import Cities, Regions


class CitiesAdmin(admin.ModelAdmin):
    list_display = ("city_title",)
    list_filter = ("city_title",)


class RegionsAdmin(admin.ModelAdmin):
    list_display = ("region_title",)
    list_filter = ("region_title",)


admin.site.register(Cities, CitiesAdmin)
admin.site.register(Regions, RegionsAdmin)
