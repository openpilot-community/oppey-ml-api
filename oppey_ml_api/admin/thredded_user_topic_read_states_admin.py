from django.contrib import admin
from oppey_ml_api.models import ThreddedUserTopicReadStates


@admin.register(ThreddedUserTopicReadStates)
class ThreddedUserTopicReadStatesAdmin(admin.ModelAdmin):
    pass
