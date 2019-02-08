from django.db import models


class ThreddedTopics(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    last_user_id = models.BigIntegerField(blank=True, null=True)
    title = models.TextField()
    slug = models.TextField(unique=True)
    messageboard_id = models.BigIntegerField()
    posts_count = models.IntegerField()
    sticky = models.BooleanField()
    locked = models.BooleanField()
    hash_id = models.CharField(max_length=20)
    moderation_state = models.IntegerField()
    last_post_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_topics'
