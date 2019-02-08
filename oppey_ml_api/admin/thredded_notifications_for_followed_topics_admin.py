from django.contrib import admin
from oppey_ml_api.models import ThreddedNotificationsForFollowedTopics


@admin.register(ThreddedNotificationsForFollowedTopics)
class ThreddedNotificationsForFollowedTopicsAdmin(admin.ModelAdmin):
    pass
