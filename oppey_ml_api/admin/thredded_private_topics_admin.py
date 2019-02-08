from django.contrib import admin
from oppey_ml_api.models import ThreddedPrivateTopics


@admin.register(ThreddedPrivateTopics)
class ThreddedPrivateTopicsAdmin(admin.ModelAdmin):
    pass
