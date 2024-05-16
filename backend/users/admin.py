from django.contrib import admin

from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)
    list_filter = ('account_status',)


admin.site.register(Users, UsersAdmin)
