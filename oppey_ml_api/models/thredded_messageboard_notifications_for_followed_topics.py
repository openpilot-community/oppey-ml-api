from django.db import models


class ThreddedMessageboardNotificationsForFollowedTopics(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    messageboard_id = models.BigIntegerField()
    notifier_key = models.CharField(max_length=90)
    enabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'thredded_messageboard_notifications_for_followed_topics'
        unique_together = (('user_id', 'messageboard_id', 'notifier_key'),)
