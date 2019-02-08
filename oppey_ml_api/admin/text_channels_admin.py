from django.contrib import admin
from oppey_ml_api.models import TextChannels


@admin.register(TextChannels)
class TextChannelsAdmin(admin.ModelAdmin):
    pass
