from django.db import models


class ThreddedUserTopicFollows(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    topic_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    reason = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thredded_user_topic_follows'
        unique_together = (('user_id', 'topic_id'),)
