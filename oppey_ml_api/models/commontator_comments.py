from django.db import models


class CommontatorComments(models.Model):
    creator_type = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    editor_type = models.CharField(max_length=255, blank=True, null=True)
    editor_id = models.IntegerField(blank=True, null=True)
    thread_id = models.IntegerField()
    body = models.TextField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    cached_votes_up = models.IntegerField(blank=True, null=True)
    cached_votes_down = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    body_markup = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commontator_comments'
