from django.db import models


class ThreddedMessageboardUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    thredded_user_detail = models.ForeignKey('ThreddedUserDetails', models.DO_NOTHING)
    thredded_messageboard = models.ForeignKey('ThreddedMessageboards', models.DO_NOTHING)
    last_seen_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_messageboard_users'
        unique_together = (('thredded_messageboard', 'thredded_user_detail'),)
