from django.db import models


class ThreddedUserTopicReadStates(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    postable_id = models.BigIntegerField()
    read_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_user_topic_read_states'
        unique_together = (('user_id', 'postable_id'),)
