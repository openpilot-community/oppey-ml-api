from django.contrib import admin
from oppey_ml_api.models import ActiveStorageAttachments


@admin.register(ActiveStorageAttachments)
class ActiveStorageAttachmentsAdmin(admin.ModelAdmin):
    pass
