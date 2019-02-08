from django.contrib import admin
from oppey_ml_api.models import ModerationCases


@admin.register(ModerationCases)
class ModerationCasesAdmin(admin.ModelAdmin):
    pass
