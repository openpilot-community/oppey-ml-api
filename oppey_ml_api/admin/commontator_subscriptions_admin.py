from django.contrib import admin
from oppey_ml_api.models import CommontatorSubscriptions


@admin.register(CommontatorSubscriptions)
class CommontatorSubscriptionsAdmin(admin.ModelAdmin):
    pass
