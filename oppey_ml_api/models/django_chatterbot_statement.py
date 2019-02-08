from django.db import models


class DjangoChatterbotStatement(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField()
    conversation = models.CharField(max_length=32)
    in_response_to = models.TextField(blank=True, null=True)
    persona = models.CharField(max_length=50)
    search_text = models.TextField()
    search_in_response_to = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_chatterbot_statement'
