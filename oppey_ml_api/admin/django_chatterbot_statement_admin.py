from django.contrib import admin
from oppey_ml_api.models import DjangoChatterbotStatement


@admin.register(DjangoChatterbotStatement)
class DjangoChatterbotStatementAdmin(admin.ModelAdmin):
    pass
