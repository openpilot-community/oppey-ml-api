from django.db import models


class ThreddedPrivateUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    private_topic_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_private_users'
