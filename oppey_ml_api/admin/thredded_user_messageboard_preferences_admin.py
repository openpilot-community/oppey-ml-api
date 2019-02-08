from django.contrib import admin
from oppey_ml_api.models import ThreddedUserMessageboardPreferences


@admin.register(ThreddedUserMessageboardPreferences)
class ThreddedUserMessageboardPreferencesAdmin(admin.ModelAdmin):
    pass
