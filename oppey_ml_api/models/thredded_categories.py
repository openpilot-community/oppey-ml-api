from django.db import models


class ThreddedCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    messageboard_id = models.BigIntegerField()
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.TextField()

    class Meta:
        managed = False
        db_table = 'thredded_categories'
        unique_together = (('messageboard_id', 'slug'),)
