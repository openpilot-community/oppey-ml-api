from django.contrib import admin
from oppey_ml_api.models import VehicleConfigPullRequests


@admin.register(VehicleConfigPullRequests)
class VehicleConfigPullRequestsAdmin(admin.ModelAdmin):
    pass
