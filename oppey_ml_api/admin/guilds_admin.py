from django.contrib import admin
from oppey_ml_api.models import Guilds


@admin.register(Guilds)
class GuildsAdmin(admin.ModelAdmin):
    pass
