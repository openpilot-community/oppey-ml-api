from django.contrib import admin
from oppey_ml_api.models import ReleaseFeatures


@admin.register(ReleaseFeatures)
class ReleaseFeaturesAdmin(admin.ModelAdmin):
    pass
