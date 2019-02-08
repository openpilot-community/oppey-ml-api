from django.contrib import admin
from oppey_ml_api.models import DjangoChatterbotTag


@admin.register(DjangoChatterbotTag)
class DjangoChatterbotTagAdmin(admin.ModelAdmin):
    pass
