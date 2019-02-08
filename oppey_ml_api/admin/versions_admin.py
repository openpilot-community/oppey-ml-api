from django.contrib import admin
from oppey_ml_api.models import Versions


@admin.register(Versions)
class VersionsAdmin(admin.ModelAdmin):
    pass
