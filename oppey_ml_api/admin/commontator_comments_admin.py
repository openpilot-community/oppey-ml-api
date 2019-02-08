from django.contrib import admin
from oppey_ml_api.models import CommontatorComments


@admin.register(CommontatorComments)
class CommontatorCommentsAdmin(admin.ModelAdmin):
    pass
