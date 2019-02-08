from django.contrib import admin
from oppey_ml_api.models import CommontatorThreads


@admin.register(CommontatorThreads)
class CommontatorThreadsAdmin(admin.ModelAdmin):
    pass
