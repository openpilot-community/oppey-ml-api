from django.contrib import admin
from oppey_ml_api.models import Streamers


@admin.register(Streamers)
class StreamersAdmin(admin.ModelAdmin):
    pass
