from django.db import models


class PullRequests(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    locked = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    body = models.CharField(max_length=255, blank=True, null=True)
    pr_created_at = models.CharField(max_length=255, blank=True, null=True)
    pr_updated_at = models.CharField(max_length=255, blank=True, null=True)
    closed_at = models.CharField(max_length=255, blank=True, null=True)
    merged_at = models.CharField(max_length=255, blank=True, null=True)
    merge_commit_sha = models.CharField(max_length=255, blank=True, null=True)
    head = models.CharField(max_length=255, blank=True, null=True)
    author_association = models.CharField(max_length=255, blank=True, null=True)
    html_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pull_requests'
