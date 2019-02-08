from django.db import models


class ThreddedUserPostNotifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    post = models.ForeignKey('ThreddedPosts', models.DO_NOTHING)
    notified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_user_post_notifications'
        unique_together = (('user', 'post'),)
