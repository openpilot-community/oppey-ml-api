from django.contrib import admin
from oppey_ml_api.models import VideoHardwareItems


@admin.register(VideoHardwareItems)
class VideoHardwareItemsAdmin(admin.ModelAdmin):
    pass
