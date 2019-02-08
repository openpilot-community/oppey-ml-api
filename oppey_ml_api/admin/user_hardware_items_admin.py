from django.contrib import admin
from oppey_ml_api.models import UserHardwareItems


@admin.register(UserHardwareItems)
class UserHardwareItemsAdmin(admin.ModelAdmin):
    pass
