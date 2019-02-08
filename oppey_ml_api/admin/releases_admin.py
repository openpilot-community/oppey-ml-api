from django.contrib import admin
from oppey_ml_api.models import Releases


@admin.register(Releases)
class ReleasesAdmin(admin.ModelAdmin):
    pass
