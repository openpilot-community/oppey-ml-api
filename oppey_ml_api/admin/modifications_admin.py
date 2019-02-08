from django.contrib import admin
from oppey_ml_api.models import Modifications


@admin.register(Modifications)
class ModificationsAdmin(admin.ModelAdmin):
    pass
