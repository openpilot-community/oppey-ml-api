from django.db import models


class ThreddedPrivatePosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    postable_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thredded_private_posts'
