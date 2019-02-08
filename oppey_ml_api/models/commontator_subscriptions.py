from django.db import models


class CommontatorSubscriptions(models.Model):
    subscriber_type = models.CharField(max_length=255)
    subscriber_id = models.IntegerField()
    thread_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'commontator_subscriptions'
        unique_together = (('subscriber_id', 'subscriber_type', 'thread_id'),)
