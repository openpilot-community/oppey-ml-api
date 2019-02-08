from django.db import models


class ThreddedUserDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    latest_activity_at = models.DateTimeField(blank=True, null=True)
    posts_count = models.IntegerField(blank=True, null=True)
    topics_count = models.IntegerField(blank=True, null=True)
    last_seen_at = models.DateTimeField(blank=True, null=True)
    moderation_state = models.IntegerField()
    moderation_state_changed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_user_details'
