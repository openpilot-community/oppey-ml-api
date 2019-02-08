from django.contrib import admin
from oppey_ml_api.models import OpenrecordMigrations


@admin.register(OpenrecordMigrations)
class OpenrecordMigrationsAdmin(admin.ModelAdmin):
    pass
