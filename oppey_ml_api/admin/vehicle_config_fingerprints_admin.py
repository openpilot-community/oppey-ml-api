from django.contrib import admin
from oppey_ml_api.models import VehicleConfigFingerprints


@admin.register(VehicleConfigFingerprints)
class VehicleConfigFingerprintsAdmin(admin.ModelAdmin):
    pass
