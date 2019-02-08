from django.contrib import admin
from oppey_ml_api.models import ThreddedNotificationsForPrivateTopics


@admin.register(ThreddedNotificationsForPrivateTopics)
class ThreddedNotificationsForPrivateTopicsAdmin(admin.ModelAdmin):
    pass
