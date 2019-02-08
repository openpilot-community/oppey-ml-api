from django.contrib import admin
from oppey_ml_api.models import RailsAdminSettings


@admin.register(RailsAdminSettings)
class RailsAdminSettingsAdmin(admin.ModelAdmin):
    pass
