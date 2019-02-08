from django.contrib import admin
from oppey_ml_api.models import Moderationcases


@admin.register(Moderationcases)
class ModerationcasesAdmin(admin.ModelAdmin):
    pass
