from django.contrib import admin
from oppey_ml_api.models import Votes


@admin.register(Votes)
class VotesAdmin(admin.ModelAdmin):
    pass
