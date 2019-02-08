from django.contrib import admin
from oppey_ml_api.models import Roles


@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    pass
