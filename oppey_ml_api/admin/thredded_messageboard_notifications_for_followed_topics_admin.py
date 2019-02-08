from django.contrib import admin
from oppey_ml_api.models import ThreddedMessageboardNotificationsForFollowedTopics


@admin.register(ThreddedMessageboardNotificationsForFollowedTopics)
class ThreddedMessageboardNotificationsForFollowedTopicsAdmin(admin.ModelAdmin):
    pass
