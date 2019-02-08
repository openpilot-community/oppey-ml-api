from django.contrib import admin
from oppey_ml_api.models import Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass
