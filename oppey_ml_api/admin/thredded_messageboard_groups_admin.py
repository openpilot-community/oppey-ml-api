from django.contrib import admin
from oppey_ml_api.models import ThreddedMessageboardGroups


@admin.register(ThreddedMessageboardGroups)
class ThreddedMessageboardGroupsAdmin(admin.ModelAdmin):
    pass
