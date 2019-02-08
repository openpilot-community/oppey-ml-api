from django.db import models


class VehicleConfigRepositories(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_config = models.ForeignKey('VehicleConfigs', models.DO_NOTHING, blank=True, null=True)
    repository = models.ForeignKey('Repositories', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    repository_branch = models.ForeignKey('RepositoryBranches', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_config_repositories'
