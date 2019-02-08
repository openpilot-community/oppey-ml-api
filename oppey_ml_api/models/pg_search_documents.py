from django.db import models


class PgSearchDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    searchable_type = models.CharField(max_length=255, blank=True, null=True)
    searchable_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pg_search_documents'
