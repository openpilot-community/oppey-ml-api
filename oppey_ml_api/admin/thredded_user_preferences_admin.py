from django.contrib import admin
from oppey_ml_api.models import ThreddedUserPreferences


@admin.register(ThreddedUserPreferences)
class ThreddedUserPreferencesAdmin(admin.ModelAdmin):
    pass
