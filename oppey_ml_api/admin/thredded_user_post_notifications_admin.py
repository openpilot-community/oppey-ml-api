from django.contrib import admin
from oppey_ml_api.models import ThreddedUserPostNotifications


@admin.register(ThreddedUserPostNotifications)
class ThreddedUserPostNotificationsAdmin(admin.ModelAdmin):
    pass
