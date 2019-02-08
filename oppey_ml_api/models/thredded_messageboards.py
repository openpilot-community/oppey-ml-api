from django.db import models


class ThreddedMessageboards(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    slug = models.TextField(unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    topics_count = models.IntegerField(blank=True, null=True)
    posts_count = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()
    last_topic_id = models.BigIntegerField(blank=True, null=True)
    messageboard_group_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    locked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'thredded_messageboards'
