from django.contrib import admin
from oppey_ml_api.models import GuideHardwareItems


@admin.register(GuideHardwareItems)
class GuideHardwareItemsAdmin(admin.ModelAdmin):
    pass
