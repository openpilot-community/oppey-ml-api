from django.contrib import admin
from oppey_ml_api.models import ThreddedMessageboardUsers


@admin.register(ThreddedMessageboardUsers)
class ThreddedMessageboardUsersAdmin(admin.ModelAdmin):
    pass
