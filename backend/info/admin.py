from django.contrib import admin

from .models import RegionalDivisions


class RegionalDivisionsAdmin(admin.ModelAdmin):
    list_display = (
        "regional_divisions_title",
        "regional_divisions_region",
    )
    list_filter = ("regional_divisions_region",)


admin.site.register(RegionalDivisions, RegionalDivisionsAdmin)
