from django.contrib import admin
from oppey_ml_api.models import ActiveStorageBlobs


@admin.register(ActiveStorageBlobs)
class ActiveStorageBlobsAdmin(admin.ModelAdmin):
    pass
