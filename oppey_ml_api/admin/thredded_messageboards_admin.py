from django.contrib import admin
from oppey_ml_api.models import ThreddedMessageboards


@admin.register(ThreddedMessageboards)
class ThreddedMessageboardsAdmin(admin.ModelAdmin):
    pass
