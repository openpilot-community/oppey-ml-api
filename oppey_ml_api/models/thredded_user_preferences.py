from django.db import models


class ThreddedUserPreferences(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    follow_topics_on_mention = models.BooleanField()
    auto_follow_topics = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_user_preferences'
