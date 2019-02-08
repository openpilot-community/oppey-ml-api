from django.contrib import admin
from oppey_ml_api.models import RepositoryBranches


@admin.register(RepositoryBranches)
class RepositoryBranchesAdmin(admin.ModelAdmin):
    pass
