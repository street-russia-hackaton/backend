from django.contrib import admin

from .models import UserPassport, Users


class UserPassportInline(admin.TabularInline):
    model = UserPassport
    extra = 0


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    """Управление пользователями"""

    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "phone",
        "account_status",
    )
    list_display_links = ("id", "email")
    search_fields = ("email", "account_status")
    inlines = [
        UserPassportInline,
    ]


@admin.register(UserPassport)
class UserPassportAdmin(admin.ModelAdmin):
    """Управление доп. информацией"""

    list_display = (
        "user",
        "passport_series",
        "passport_number",
        "accept_rules",
    )
    list_display_links = ("user",)
    search_fields = ("user",)
    empty_value_display = "-пусто-"
