from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "news_title",
        "created_at",
    )
    list_filter = (
        "news_regional_divisions",
        "news_disciplines",
        "news_author",
    )
