from django.contrib import admin
from oppey_ml_api.models import Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
