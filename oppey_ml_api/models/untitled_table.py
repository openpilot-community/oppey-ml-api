from django.db import models


class UntitledTable(models.Model):
    column2 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'untitled_table'
