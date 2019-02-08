from django.contrib import admin
from oppey_ml_api.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass
