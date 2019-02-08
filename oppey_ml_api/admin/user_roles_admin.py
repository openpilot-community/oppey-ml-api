from django.contrib import admin
from oppey_ml_api.models import UserRoles


@admin.register(UserRoles)
class UserRolesAdmin(admin.ModelAdmin):
    pass
