from django.contrib import admin

from authentication.models.location import Location
from authentication.models.user import User

admin.site.register(User)
admin.site.register(Location)
