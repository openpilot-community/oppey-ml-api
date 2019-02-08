from django.contrib import admin
from oppey_ml_api.models import Transactions


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    pass
