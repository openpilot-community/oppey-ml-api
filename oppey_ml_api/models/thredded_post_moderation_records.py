from django.db import models


class ThreddedPostModerationRecords(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField(blank=True, null=True)
    messageboard_id = models.BigIntegerField(blank=True, null=True)
    post_content = models.TextField(blank=True, null=True)
    post_user_id = models.BigIntegerField(blank=True, null=True)
    post_user_name = models.TextField(blank=True, null=True)
    moderator_id = models.BigIntegerField(blank=True, null=True)
    moderation_state = models.IntegerField()
    previous_moderation_state = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_post_moderation_records'
