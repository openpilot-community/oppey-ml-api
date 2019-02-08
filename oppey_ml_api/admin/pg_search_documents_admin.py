from django.contrib import admin
from oppey_ml_api.models import PgSearchDocuments


@admin.register(PgSearchDocuments)
class PgSearchDocumentsAdmin(admin.ModelAdmin):
    pass
