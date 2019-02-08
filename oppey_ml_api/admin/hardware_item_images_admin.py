from django.contrib import admin
from oppey_ml_api.models import HardwareItemImages


@admin.register(HardwareItemImages)
class HardwareItemImagesAdmin(admin.ModelAdmin):
    pass
