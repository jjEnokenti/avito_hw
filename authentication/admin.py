from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from authentication.models.location import Location


class UserAdminPage(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal Info',
            {'fields': ('first_name', 'last_name', 'email', 'age', 'role')}
        ),
        (
            'Permission',
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
        ),
        (
            'Important dates',
            {'fields': ('last_login', 'date_joined')}
        )
    )


user = get_user_model()
admin.site.register(user, UserAdminPage)
admin.site.register(Location)
