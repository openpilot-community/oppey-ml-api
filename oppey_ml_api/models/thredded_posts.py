from django.db import models


class ThreddedPosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=191, blank=True, null=True)
    postable_id = models.BigIntegerField()
    messageboard_id = models.BigIntegerField()
    moderation_state = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_posts'
