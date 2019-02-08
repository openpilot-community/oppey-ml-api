from django.contrib import admin
from oppey_ml_api.models import VehicleConfigRepositories


@admin.register(VehicleConfigRepositories)
class VehicleConfigRepositoriesAdmin(admin.ModelAdmin):
    pass
