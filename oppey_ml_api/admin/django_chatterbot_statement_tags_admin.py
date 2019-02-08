from django.contrib import admin
from oppey_ml_api.models import DjangoChatterbotStatementTags


@admin.register(DjangoChatterbotStatementTags)
class DjangoChatterbotStatementTagsAdmin(admin.ModelAdmin):
    pass
