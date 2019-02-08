from django.contrib import admin
from oppey_ml_api.models import ThreddedPostModerationRecords


@admin.register(ThreddedPostModerationRecords)
class ThreddedPostModerationRecordsAdmin(admin.ModelAdmin):
    pass
