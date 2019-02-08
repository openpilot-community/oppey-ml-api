from django.contrib import admin
from oppey_ml_api.models import HardwareTypes


@admin.register(HardwareTypes)
class HardwareTypesAdmin(admin.ModelAdmin):
    pass
