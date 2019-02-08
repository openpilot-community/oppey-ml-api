from django.contrib import admin
from oppey_ml_api.models import ThreddedUserPrivateTopicReadStates


@admin.register(ThreddedUserPrivateTopicReadStates)
class ThreddedUserPrivateTopicReadStatesAdmin(admin.ModelAdmin):
    pass
