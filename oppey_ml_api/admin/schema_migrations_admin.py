from django.contrib import admin
from oppey_ml_api.models import SchemaMigrations


@admin.register(SchemaMigrations)
class SchemaMigrationsAdmin(admin.ModelAdmin):
    pass
