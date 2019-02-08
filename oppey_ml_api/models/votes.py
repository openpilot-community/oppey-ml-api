from django.db import models


class Votes(models.Model):
    votable_type = models.CharField(max_length=255, blank=True, null=True)
    votable_id = models.IntegerField(blank=True, null=True)
    voter_type = models.CharField(max_length=255, blank=True, null=True)
    voter_id = models.IntegerField(blank=True, null=True)
    vote_flag = models.NullBooleanField()
    vote_scope = models.CharField(max_length=255, blank=True, null=True)
    vote_weight = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'votes'
