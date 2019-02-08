from django.db import models


class VehicleConfigPullRequests(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_config = models.ForeignKey('VehicleConfigs', models.DO_NOTHING, blank=True, null=True)
    pull_request = models.ForeignKey('PullRequests', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehicle_config_pull_requests'
