from django.contrib import admin
from oppey_ml_api.models import Repositories


@admin.register(Repositories)
class RepositoriesAdmin(admin.ModelAdmin):
    pass
