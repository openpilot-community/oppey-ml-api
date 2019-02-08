from django.db import models


class VehicleConfigs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    vehicle_make = models.ForeignKey('VehicleMakes', models.DO_NOTHING, blank=True, null=True)
    vehicle_model = models.ForeignKey('VehicleModels', models.DO_NOTHING, blank=True, null=True)
    vehicle_trim = models.ForeignKey('VehicleSpecs', models.DO_NOTHING, blank=True, null=True)
    vehicle_config_status = models.ForeignKey('VehicleConfigStatuses', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    vehicle_make_package = models.ForeignKey('VehicleMakePackages', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    vehicle_config_type = models.ForeignKey('VehicleConfigTypes', models.DO_NOTHING, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    children_count = models.IntegerField(blank=True, null=True)
    year_end = models.IntegerField(blank=True, null=True)
    trim_styles_count = models.IntegerField(blank=True, null=True)
    refreshing = models.NullBooleanField()
    cached_votes_total = models.IntegerField(blank=True, null=True)
    cached_votes_score = models.IntegerField(blank=True, null=True)
    cached_votes_up = models.IntegerField(blank=True, null=True)
    cached_votes_down = models.IntegerField(blank=True, null=True)
    cached_weighted_score = models.IntegerField(blank=True, null=True)
    cached_weighted_total = models.IntegerField(blank=True, null=True)
    cached_weighted_average = models.FloatField(blank=True, null=True)
    primary_repository = models.ForeignKey('Repositories', models.DO_NOTHING, blank=True, null=True)
    primary_pull_request = models.ForeignKey('PullRequests', models.DO_NOTHING, blank=True, null=True)
    source_image_url = models.CharField(max_length=255, blank=True, null=True)
    user_count = models.IntegerField(blank=True, null=True)
    views_count = models.IntegerField()
    followers_count = models.IntegerField()
    thredded_messageboard_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_configs'
        unique_together = (('year', 'year_end', 'vehicle_make', 'vehicle_model', 'vehicle_config_type'),)
