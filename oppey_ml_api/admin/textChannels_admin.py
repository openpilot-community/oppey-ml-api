from django.contrib import admin
from oppey_ml_api.models import Textchannels


@admin.register(Textchannels)
class TextchannelsAdmin(admin.ModelAdmin):
    pass
